from flask import request
from flask_restful import Resource

from data.users import Users


class User(Resource):
    def get(self, name=None):
        user_data = Users.objects([] if name is None else name)
        user_data = [user.to_json() for user in user_data]

        

        if name is None:
            return {'users': user_data}, 200
        else:
            if len(user_data) < 1:
                return {}, 404 
            return {'user': user_data[0].to_json()}, 200

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201
