from flask import request
from flask_restful import Resource


class Post(Resource):
    def get(self):
        num = int(request.args['number'])
        return {}
