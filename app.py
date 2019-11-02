from flask import Flask
from api import CatApi

from data.comments import Comment
from data.posts import Post
from data.users import User

from classes import User, Post


app = Flask(__name__)

api = CatApi(app, catch_all_404s=True)


api.add_resource(User, '/user')
api.add_resource(Post, '/post')

if __name__ == "__main__":
    app.run(debug=True)
