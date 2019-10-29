from flask import jsonify
from flask_restful import Api


class CatApi(Api):
    def handle_error(self, e):
        if e.code == 404:
            msg = 'You picked the wrong house, fool!'
        else:
            msg = 'Meow'
        return jsonify({'message': msg}), e.code
