from datetime import datetime

from flask import request
from flask_restful import abort, Resource
from mongoengine.errors import NotUniqueError, ValidationError

from data.users import Users
from resources.authorization import hash_string_with_salt, token_required, validate_values_in_dictionary


class User(Resource):
    @token_required
    def get(current_user, self, name=None):
        if name is None and not current_user.is_admin:
            abort(401, message="Missing rights. Try /user/<username> for user info.")

        kwarg = {} if name is None else {'name': name}
        user_data = Users.objects(**kwarg)
        user_data = [user.to_json() for user in user_data]

        if name is None:
            return {'users': user_data}, 200
        else:
            if len(user_data) < 1:
                abort(404, message="User '{}' doesn't exist".format(name))
            return {'user': user_data[0]}, 200

    def post(self, name=None):
        if name is not None:
            abort(405, message="Can't POST to this endpoint. Try /user")

        received_json = request.get_json()
        errors = validate_values_in_dictionary(received_json, Users,
            required_keys={'name', 'email', 'password'}, sensitive_keys={'name'}, unique_keys={'name', 'email'})
        if errors:
            abort(400, errors=errors)

        name = received_json['name']
        email = received_json['email']
        hashed_password = hash_string_with_salt(received_json['password'])

        try:
            new_user = Users(
                active=True,
                is_admin=False,
                name=name,
                email=email,
                password=hashed_password,
                registered_datetime=datetime.utcnow(),
                posts=[],
                comments=[]
            ).save()
        except ValidationError as e:
            abort(400, errors=str(e))

        return {'message': "User '{}' registered successfully".format(new_user.name),
                'user': new_user.to_json()}, 201

    @token_required
    def put(current_user, self, name=None):
        if name is None:
            abort(405, message="Can't PUT to this endpoint. Try /user/<username>")
        if current_user.name != name and not current_user.is_admin:
            abort(401, message="Missing rights.")

        existing_user = Users.objects(name=name).first()
        if existing_user is None:
            abort(404, message="User '{}' doesn't exist".format(name))

        received_json = request.get_json()
        errors = validate_values_in_dictionary(received_json, Users, sensitive_keys={'name'}, unique_keys={'name', 'email'},
                                               admin=current_user.is_admin, admin_keys={'active', 'is_admin', 'name'})
        if errors:
            abort(400, errors=errors)

        if received_json.get('active')      is not None: existing_user.active = bool(received_json.get('active'))
        if received_json.get('is_admin')    is not None: existing_user.is_admin = bool(received_json.get('is_admin'))
        if received_json.get('name')        is not None: existing_user.name = received_json.get('name')

        if received_json.get('email')       is not None: existing_user.email = received_json.get('email')
        if received_json.get('password')    is not None: existing_user.password = hash_string_with_salt(received_json.get('password'))

        existing_user.save()

        return {}, 204

    @token_required
    def delete(current_user, self, name=None):
        if name is None:
            abort(405, message="Can't DELETE at this endpoint. Try /user/<username>")
        if current_user.name != name and not current_user.is_admin:
            abort(401, message="Missing rights.")

        existing_user = Users.objects(name=name).first()

        if existing_user is None:
            abort(404, message="User '{}' doesn't exist".format(name))

        existing_user.delete()

        return {}, 204
