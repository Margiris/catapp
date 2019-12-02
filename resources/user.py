from datetime import datetime

from flask import request
from flask_restful import abort, Resource

from data.users import Users
from resources.authorization import hash_string_with_salt, token_required


class User(Resource):
    @token_required
    def get(current_user, self, name=None):
        if name is None and not current_user.is_admin:
            abort(401, message='Nothing to see here. Try /user/<username> for user info.')

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

        received_data = request.get_json()
        name = received_data['name']

        if len(Users.objects(name=name)) >= 1:
            abort(409, message="User '{}' already exists".format(name))

        email = received_data['email']
        hashed_password = hash_string_with_salt(received_data['password'])

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

        return {'message': "User '{}' registered successfully".format(new_user.name),
                'user': new_user.to_json()}, 201

    @token_required
    def put(current_user, self, name=None):
        if name is None:
            abort(405, message="Can't PUT to this endpoint. Try /user/<username>")

        existing_user = Users.objects(name=name).first()

        if existing_user is None:
            abort(404, message="User '{}' doesn't exist".format(name))

        received_data = request.get_json()
        new_name = received_data.get('name')

        if len(Users.objects(name=new_name)) >= 1:
            abort(409, message="User '{}' already exists".format(name))

        if received_data.get('active') is not None: existing_user.active = bool(received_data.get('active'))
        if received_data.get('is_admin') is not None: existing_user.is_admin = bool(received_data.get('is_admin'))
        if received_data.get('name') is not None: existing_user.name = received_data.get('name')

        if received_data.get('email') is not None: existing_user.email = received_data.get('email')
        if received_data.get('password') is not None: existing_user.password = hash_string_with_salt(received_data.get('password'))

        existing_user.save()

        return {}, 204

    @token_required
    def delete(current_user, self, name=None):
        if name is None:
            abort(405, message="Can't DELETE at this endpoint. Try /user/<username>")

        existing_user = Users.objects(name=name).first()

        if existing_user is None:
            abort(404, message="User '{}' doesn't exist".format(name))

        existing_user.delete()

        return {}, 204
