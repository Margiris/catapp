from flask import request
from flask_restful import abort, Resource

from data.ratings import Ratings
from data.comments import Comments
from data.posts import Posts


class Post(Resource):
    def get(self, id=None):
        if id is not None and len(id) != 24:
            abort(404, message="{} is not a valid post id".format(id))

        kwarg = {} if id is None else {'id': id}
        post_data = Posts.objects(**kwarg)
        post_data = [post.to_json() for post in post_data]

        if id is None:
            return {'posts': post_data}, 200
        else:
            if len(post_data) < 1:
                abort(404, message="Post with id '{}' doesn't exist".format(id))
            return {'post': post_data[0]}, 200
