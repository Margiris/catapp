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
from data.expired_tokens import ExpiredTokens
from secrets import app_secret_key, token_expiration_time


class Login(Resource):
    def get(self):
        auth = request.authorization
        user = Users.objects(name=auth.username).first()

        if not auth or not auth.username or not auth.password or user is None or not verify_password(user.password, auth.password):
            # TODO maybe abort() with headers
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

        if not user.active:
            abort(401, message='Your account has been banned. Please contact the moderators if you feel that was a mistake.')

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
            assert ExpiredTokens.objects(token=token).first() is None

            payload = decode(token, app_secret_key)
            assert payload['exp'] > timegm(datetime.utcnow().utctimetuple())
            assert payload['iat'] > timegm(
                (datetime.utcnow() - token_expiration_time).utctimetuple())

            current_user = Users.objects(id=payload['sub']).first()

            assert current_user is not None
            assert current_user.active is True
        except Exception as e:
            abort(401, message='Token is missing, invalid or expired')

        return f(current_user, *args, **kwargs)

    return decorated


def validate_values_in_dictionary(dictionary, module_class, required_keys={}, sensitive_keys={}, illegal_chars=['/', '\\'], unique_keys={}, admin_keys={}, admin=False):
    # check for missing data and add to errors dict if found
    errors = {key: '{} is required'.format(
        key.title()) for key in required_keys if key not in dictionary}

    # exclude keys with errors from further validation
    admin_keys = {key for key in admin_keys if key not in errors}
    # check if user has rights to keys and append to errors dict if not
    if not admin:
        errors = {**errors,
                  **{key: "Missing rights for '{}' property".format(key) for key in admin_keys if key in dictionary}}

    # check if provided password is safe enough and append to errors dict if not
    if len(dictionary.get('password', "12345678")) < 8:
        errors['password'] = 'Password must be at least 8 characters long'

    # exclude keys with errors from further validation
    sensitive_keys = {key for key in sensitive_keys if key not in errors}
    # check for illegal characters and append to errors dict if found
    errors = {**errors,
              **{key: '{} contains illegal characters'.format(key.title()) for key in sensitive_keys if any(
                  char in dictionary.get(key, "") for char in illegal_chars)}}

    # exclude keys with errors from further validation
    unique_keys = {key for key in unique_keys if key not in errors}
    # find duplicates of unique keys in database and append to errors dict if found
    errors = {**errors,
              **{key: '{} already exists'.format(key.title()) for key in unique_keys if len(
                  module_class.objects(**{key: dictionary.get(key, "")})) >= 1}}

    return errors

def logout(token):
    ExpiredTokens(
        token=token
    ).save()


class Logout(Resource):
    @token_required
    def get(current_user, self):
        token = request.headers['authorization'][7:]
        logout(token)

        return {}, 204
