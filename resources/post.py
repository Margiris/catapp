from flask import request
from flask_restful import Resource

from data.ratings import Ratings
from data.comments import Comments
from data.posts import Posts


class Post(Resource):
    def get(self):
        num = int(request.args['number'])
        return {}
