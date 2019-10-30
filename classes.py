from flask import Flask, request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from app import db

# class Team(Resource):
#     def post(self, team_id=None, player_id=None):
#         if team_id is None and player_id is None:
#             # first version
#         if team_id is not None and player_id is None:
#             # second version
#         if team_id is not None and player_id is not None:
#             # third version


class User(db.Model, Resource):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

    def get(self):
        num = int(request.args['number'])
        return {}

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201
