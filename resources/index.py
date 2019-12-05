from flask_restful import Resource

class Index(Resource):
    def get(self):
        return "Margiris's Cat Pics site"