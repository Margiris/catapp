from base64 import b64decode
from tempfile import TemporaryFile

from flask import request
from flask_restful import abort, Resource

from data.ratings import Ratings
from data.comments import Comments
from data.posts import Posts
from resources.authorization import token_required, validate_values_in_dictionary


class Post(Resource):
    def get(self, id=None):
        if id is not None and (not isinstance(id, str) or len(id) != 24):
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

    @token_required
    def post(current_user, self, id=None):
        if id is not None:
            abort(405, message="Can't POST to this endpoint. Try /post")

        received_json = request.get_json()
        errors = validate_values_in_dictionary(received_json, Posts, required_keys={
                                               'title', 'image'}, sensitive_keys={'title'})
        if errors:
            abort(400, errors=errors)

        try:
            new_post = Posts(
                title=received_json['title'],
                author=current_user,
                comments=[],
                rating=Ratings()
            )

            image64 = received_json['image']
            file_like = b64decode(image64)
            bytes_image = bytearray(file_like)

            with TemporaryFile() as f:
                f.write(bytes_image)
                f.flush()
                f.seek(0)
                new_post.image.put(f)
            new_post.save()

            current_user.posts.append(new_post)
            current_user.save()
        except Exception as e:
            abort(400, errors=str(e))

        return {'message': "Post successful", 'post': new_post.to_json()}, 201

    @token_required
    def put(current_user, self, id=None):
        if id is None:
            abort(405, message="Can't PUT to this endpoint. Try /post/<post id>")
        elif not isinstance(id, str) or len(id) != 24:
            abort(404, message="{} is not a valid post id".format(id))

        existing_post = Posts.objects(id=id).first()
        if existing_post is None:
            abort(404, message="Post with id '{}' doesn't exist".format(id))

        if current_user != existing_post.author and not current_user.is_admin:
            abort(401, message="Missing rights.")

        received_json = request.get_json()
        errors = validate_values_in_dictionary(
            received_json, Posts, sensitive_keys={'title'}, admin_keys={'image'}, admin=current_user.is_admin)
        if errors:
            abort(400, errors=errors)

        if received_json.get('title') is not None:
            existing_post.title = received_json.get('title')
        if received_json.get('image') is not None:
            image64 = received_json['image']
            file_like = b64decode(image64)
            bytes_image = bytearray(file_like)

            with TemporaryFile() as f:
                f.write(bytes_image)
                f.flush()
                f.seek(0)
                existing_post.image.replace(f)

        existing_post.save()

        return {}, 204

    @token_required
    def delete(current_user, self, id=None):
        if id is None:
            abort(405, message="Can't DELETE at this endpoint. Try /post/<post id>")
        elif not isinstance(id, str) or len(id) != 24:
            abort(404, message="{} is not a valid post id".format(id))

        existing_post = Posts.objects(id=id).first()
        if existing_post is None:
            abort(404, message="Post '{}' doesn't exist".format(id))

        if current_user.name != existing_post.author.name and not current_user.is_admin:
            abort(401, message="Missing rights.")

        existing_post.author.posts.remove(existing_post)
        existing_post.author.save()
        existing_post.delete()

        return {}, 204
