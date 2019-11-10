from flask import request
from flask_restful import abort, Resource


class GitHub(Resource):
    def get(self):
        print('get')
        print(request.args.get())

    def post(self):
        print('post')
        print(request.args.get())

    def put(self):
        print('put')
        print(request.args.get())

    def patch(self):
        print('patch')
        print(request.args.get())
