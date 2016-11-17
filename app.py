from flask import Flask, jsonify

app = Flask(__name__)

games = [
    {
        name: 'angle',

        score: [],

        students : []

    }
]

# POST /game data: {gamename: }
@app.route('/game', methods=['POST'])
def create_game():
    pass



# GET /game/<string: gamename>
@app.route('/game/<string:name>') # the stringname situation is specfic to flask because it means that some name can be filled in
def get_game(name):
    pass



# GET /game (All)
@app.route('/game')
def get_games():
    return jsonify({'games': games}) #converts the games into json. But we need the json to be an object so we are making our games array the value of a key. {games: games}



# POST /game/<string: gamename>/item
@app.route('/game/<string:name>/item', methods=['POST'])
def create_item_in_game(name):
    pass


#GET /store/<string:name>/item
@app.route('/game/<string:name>/item')
def get_item_in_game(name):
    pass


app.run(port=5000)
