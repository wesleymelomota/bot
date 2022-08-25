from flask import Flask
from flask_restful import Resource, Api
from scraper import bot


app = Flask(__name__)
api = Api(app)


class NoteLenovo(Resource):
    def get(self):
        return {'notebooks_Lenovo': bot()}

api.add_resource(NoteLenovo, '/notebooks/lenovo')


if __name__ == '__main__':
    app.run()