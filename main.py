from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

from secrets import app_secret_key, db_local_ip, db_debug_ip

from resources.user import User
from resources.post import Post
from resources.user_post import UserPost
from resources.user_post_comment import UserPostComment
from resources.comment import Comment
from resources.authorization import Login, Logout


app = Flask(__name__)

app.config['SECRET_KEY'] = app_secret_key
app.config['MONGODB_SETTINGS'] = {
    'alias': 'core',
    'db': 'catpic',
    'host': db_debug_ip if __name__ == "__main__" else db_local_ip,
    'port': 27017
}

# errors = {
#     'NotFound': {
#         'message': "You picked the wrong house, fool!",
#         'status': 404
#     }
# }

api = Api(app, catch_all_404s=True)  # , errors=errors)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

api.add_resource(Login,             '/login', endpoint='login')
api.add_resource(Logout,            '/logout', endpoint='logout')

api.add_resource(User,              # '/users',
                                    '/user',
                                    '/user/<string:name>', endpoint='user')

api.add_resource(Post,              # '/posts',
                                    '/post',
                                    '/post/<string:post_id>', endpoint='post')

api.add_resource(Comment,           '/post/<string:post_id>/comment',
                                    '/post/<string:post_id>/comment/<string:comment_id>', endpoint='comment')

api.add_resource(UserPost,          '/user/<string:name>/post',
                                    '/user/<string:name>/post/<string:post_id>', endpoint='user_post')

api.add_resource(UserPostComment,   '/user/<string:name>/post/<string:post_id>/comment',
                                    '/user/<string:name>/post/<string:post_id>/comment/<string:comment_id>', endpoint='user_post_comment')
if __name__ == "__main__":
    app.run(debug=True)
