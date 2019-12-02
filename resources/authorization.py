from datetime import datetime, timedelta
from os import urandom
from binascii import hexlify
from hashlib import sha256, pbkdf2_hmac

from flask import request, make_response
from flask_restful import abort, Resource
import jwt

from data.users import Users
from secrets import app_secret_key


class Login(Resource):
    def get(self):
        auth = request.authorization
        user = Users.objects(name=auth.username).first()

        if not auth or not auth.username or not auth.password or user is None or not verify_password(user.password, auth.password):
            print(auth.username, auth.password, user.name, verify_password(user.password, auth.password))
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

        token = jwt.encode({'id': str(user.id), 'expiration': str(datetime.utcnow() + timedelta(minutes=30))}, app_secret_key)

        return {'token': token.decode('UTF-8')}

    def post(self):
        print('post')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

    def put(self):
        print('put')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

    def patch(self):
        print('patch')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}


def hash_string_with_salt(a_string, salt=None):
    if salt is None:
        salt = sha256(urandom(60)).hexdigest()

    salt = salt.encode('ascii')
    str_hash = hexlify(pbkdf2_hmac(
        'sha512', a_string.encode('utf-8'), salt, 100000))
    return (salt + str_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    return stored_password == hash_string_with_salt(provided_password, salt)


def wrong_credentials_response(message='Could not verify'):
    return make_response(message, 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
    # return {'message': 'Wrong username or password'}, 401
