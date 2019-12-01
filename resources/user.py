from datetime import datetime
from flask import request
from flask_restful import abort, Resource

from data.users import Users
from resources.auth import hash_string_with_salt


class User(Resource):
    def get(self, name=None):
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
            abort(405, message="Can't post to this endpoint. Try /user")

        received_data = request.get_json()
        hashed_password = hash_string_with_salt(received_data['password'])

        new_user = Users(
            active=True,
            is_admin=False,
            name=received_data['name'],
            email=received_data['email'],
            password=hashed_password,
            registered_datetime=datetime.utcnow(),
            posts=[],
            comments=[]
        ).save()

        return {'message': "User '{}' registered successfully".format(new_user.name),
                'user': new_user.to_json()}, 201
