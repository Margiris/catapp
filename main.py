from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

from resources.post import Post
from resources.user import User


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'alias': 'core',
    'db': 'catpic',
    'host': '192.168.0.102' if __name__ == "__main__" else '127.0.0.1',
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

api.add_resource(User,  # '/users',
                        '/user',
                        '/user/<string:name>', endpoint='user')
api.add_resource(Post,  # '/posts',
                        '/post',
                        '/post/<string:name>', endpoint='post')

if __name__ == "__main__":
    app.run(debug=True)
