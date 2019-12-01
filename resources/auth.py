from flask import request
from flask_restful import abort, Resource

class Login(Resource):
    def get(self):
        print('get')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

    def post(self):
        print('post')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

    def put(self):
        print('put')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

    def patch(self):
        print('patch')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}
