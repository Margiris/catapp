from flask import request
from flask_restful import abort, Resource

from data.ratings import Ratings
from data.comments import Comments
from data.posts import Posts
from resources.authorization import token_required, validate_values_in_dictionary

class Comment(Resource):
    def get(self, post_id, id=None):
        if id is not None and isinstance(id, str) and len(id) != 24:
            abort(404, message="{} is not a valid comment id".format(id))

        post_data = Posts.objects(id=post_id).first()
        if post_data is None:
            abort(404, message="Post with id '{}' doesn't exist".format(post_id))
        
        if id is None:
            comment_data = [comment.to_json() for comment in post_data.comments]
            return {"post '{}' comments".format(post_id): comment_data}, 200
        else:
            comment_data = [comment.to_json() for comment in post_data.comments if str(comment.id) == id]
            if len(comment_data) < 1:
                abort(404, message="Comment with id '{}' doesn't exist".format(id))
            return {"post '{}' comment": comment_data[0]}, 200

    @token_required
    def post(current_user, self, post_id, id=None):
        if id is not None:
            abort(405, message="Can't POST to this endpoint. Try /post/<post id>/comment")

        post_data = Posts.objects(id=post_id).first()
        if post_data is None:
            abort(404, message="Post with id '{}' doesn't exist".format(post_id))
        
        received_json = request.get_json()
        errors = validate_values_in_dictionary(received_json, Comments, required_keys={'body'})
        if errors:
            abort(400, errors=errors)

        try:
            new_comment = Comments(
                author=current_user,
                body=received_json['body'],
                rating=Ratings()
            )
            post_data.comments.append(new_comment)
            post_data.save()
        except Exception as e:
            abort(400, errors=str(e))

        return {'message': "Comment posted successfully", 'comment': new_comment.to_json()}, 201
