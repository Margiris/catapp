from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from api import CatApi
from classes import HelloWorld, Multi, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

api = CatApi(app, catch_all_404s=True)

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi')
api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True)
