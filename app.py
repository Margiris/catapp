from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from api import CatApi

from resources.post import Post
from resources.user import User


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'alias': 'core',
    'db': 'catpic',
    'host': '192.168.0.102',
    'port': 27017
}

api = CatApi(app, catch_all_404s=True)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

api.add_resource(User,  '/users',
                        '/user/<string:name>')
api.add_resource(Post,  '/posts',
                        '/post/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)
