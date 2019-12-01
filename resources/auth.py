from os import urandom
from binascii import hexlify
from hashlib import sha256, pbkdf2_hmac

from flask import request
from flask_restful import abort, Resource


class Login(Resource):
    def get(self):
        print('get')
        [print(arg, request.args.get(arg)) for arg in request.args]
        return {}

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
