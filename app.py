from flask import Flask, request
from api import CatApi
from classes import HelloWorld, Multi, User


app = Flask(__name__)
api = CatApi(app, catch_all_404s=True)

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi')
api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True)
