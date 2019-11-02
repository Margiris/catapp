# from datetime import datetime
from flask import Flask, request
from flask_restful import Resource
# from app import db

# class Team(Resource):
#     def post(self, team_id=None, player_id=None):
#         if team_id is None and player_id is None:
#             # first version
#         if team_id is not None and player_id is None:
#             # second version
#         if team_id is not None and player_id is not None:
#             # third version


class User(Resource):
    def get(self):
        num = int(request.args['number'])
        return {}

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201


class Post(Resource):
    def get(self):
        num = int(request.args['number'])
        return {}
