from flask import jsonify


class CatApi(Api):
    def handle_error(self, e):
        if e.code == 404:
            msg = 'You picked the wrong house, fool!'
        else:
            msg = 'Oops'
        return jsonify({'message': msg}), e.code
