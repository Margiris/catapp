# from datetime import datetime
from flask import Flask, request
from flask_restful import Resource
# from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
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
    # __tablename__ = "user"
    # id = Column('id', Integer, primary_key=True)
    # public_id = Column('public_id', Integer, unique=True, nullable=False)
    # email = Column('email', String(120), unique=True, nullable=False)
    # username = Column('username', String(15), unique=True, nullable=False)
    # password = Column('password', String(60), nullable=False)
    # avatar = Column('avatar', String(20), nullable=False,
    #                    default='default_avatar.png')
    # is_admin = Column('admin', Boolean)
    # posts = relationship('Post', backref='author', lazy=True)

    # def __repr__(self):
    #     return f"User('{self.public_id}', '{self.username}', '{self.email}', '{self.is_admin}', '{self.avatar}')"

    def get(self):
        num = int(request.args['number'])
        return {}

    def post(self):
        received_data = request.get_json()
        print(received_data)
        return {'received': received_data}, 201


class Post(Resource):
    # id = Column(Integer, primary_key=True)
    # title = Column(String(100), nullable=False)
    # image = Column(String(20), nullable=False)
    # datetime_posted = Column(
    #     DateTime, nullable=False, default=datetime.utcnow)
    # user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    # def __repr__(self):
    #     return f"Post('{self.datetime_posted}', '{self.title}', '{self.image}')"

    def get(self):
        num = int(request.args['number'])
        return {}
