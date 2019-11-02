from flask import Flask
from api import CatApi

from data.comments import Comments
from data.posts import Posts
from data.users import Users

from resources.post import Post
from resources.user import User


app = Flask(__name__)

api = CatApi(app, catch_all_404s=True)


api.add_resource(User, '/users', '/user/<int:id>')
api.add_resource(Post, '/post')

if __name__ == "__main__":
    app.run(debug=True)
