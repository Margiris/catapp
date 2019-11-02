from flask import request
from flask_restful import Resource


class User(Resource):
    def get(self):
        num = int(request.args['number'])
        return {}

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201
