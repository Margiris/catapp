from binascii import hexlify
from calendar import timegm
from datetime import datetime, timedelta
from functools import wraps
from hashlib import sha256, pbkdf2_hmac
from os import urandom

from flask import request, make_response
from flask_restful import abort, Resource
from jwt import encode, decode

from data.users import Users
from secrets import app_secret_key, token_expiration_time


class Login(Resource):
    def get(self):
        auth = request.authorization
        user = Users.objects(name=auth.username).first()

        if not auth or not auth.username or not auth.password or user is None or not verify_password(user.password, auth.password):
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
            # TODO ^ maybe abort() with headers
        token = encode({
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow(),
            'sub': str(user.id)
        }, app_secret_key)

        return {'token': token.decode('UTF-8')}, 200


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


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers['authorization'][7:]
            payload = decode(token, app_secret_key)

            assert payload['exp'] > timegm(datetime.utcnow().utctimetuple())
            assert payload['iat'] > timegm(
                (datetime.utcnow() - token_expiration_time).utctimetuple())

            current_user = Users.objects(id=payload['sub']).first()
        except Exception as e:
            print(repr(e))
            return {'message': 'Token is missing, invalid or expired'}, 401

        return f(current_user, *args, **kwargs)

    return decorated


class Logout(Resource):
    def get(self):
        return {}
