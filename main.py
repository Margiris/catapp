from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_dance.contrib.github import make_github_blueprint, github

from secrets import app_secret_key, github_client_id, github_client_secret

from resources.auth import GitHub
from resources.post import Post
from resources.user import User


app = Flask(__name__)

app.config['SECRET_KEY'] = app_secret_key
app.config['MONGODB_SETTINGS'] = {
    'alias': 'core',
    'db': 'catpic',
    'host': '192.168.0.102' if __name__ == "__main__" else '127.0.0.1',
    'port': 27017
}

github_blueprint = make_github_blueprint(client_id=github_client_id, client_secret=github_client_secret)

# errors = {
#     'NotFound': {
#         'message': "You picked the wrong house, fool!",
#         'status': 404
#     }
# }

api = Api(app, catch_all_404s=True)  # , errors=errors)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

api.add_resource(GitHub,  '/login/github', endpoint='github_login')
api.add_resource(User,  # '/users',
                        '/user',
                        '/user/<string:name>', endpoint='user')
api.add_resource(Post,  # '/posts',
                        '/post',
                        '/post/<string:id>', endpoint='post')

if __name__ == "__main__":
    app.run(debug=True)
