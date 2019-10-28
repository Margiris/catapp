from flask import Flask, request
from flask_restful import Resource, Api


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hi World'}

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201


class Multi(Resource):
    def get(self):
        print(request.args)
        num = int(request.args['number'])
        return {'result': num*8}


class User(Resource):
    def get(self):
        return {}
