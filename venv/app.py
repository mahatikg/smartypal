from flask import Flask
from flask_restful import Resource, Api

## each game is a resource, a thing that our api can return

app = Flask(__name__)
api = Api(app)


class Game(Resource):
    def get(self, gamename):
        return { 'game' : gamename}


api.add_resource(Game, '/game/<string:gamename>')


app.run(port=5000)
