from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {
        'gamename': 'anglegame',
        'scores': [
            'attempt' : 4,
            'score_num': 98
        ]
    },
    {
        'game' : 'circlegame',
        'scores': []
    }

]

# GET /game (All)
@app.route('/games')
def get_games():
    return jsonify({'games': games}) #converts the games into json. But we need the json to be an object so we are making our games array the value of a key. {games: games}

# POST /game data: {gamename: } to add a new game to the data
@app.route('/game', methods=['POST'])
def create_game():
    request_data = request.get_json()
    new_Game = {
        'name' : request_data['gamaname'],
        scores: []
    }
    games.append(new_game)
    return jsonify(new_game)


# GET /game/<string: gamename> get a specifc game
@app.route('/game/<string:gamename>') # stringname specfic to flask:means some name can be filled in
def get_game(gamename):
    for game in games:
        if game['gamename'] ==  gamename:
            return jsonify(game)
        return jsonify({message : 'game not found'})


# POST /game/<string: gamename>/score to add a new scores to a game's scores
@app.route('/game/<string:name>/score', methods=['POST'])
def create_item_in_game(gamename):
    request_data = request.get_json()
    for game in games:
        if game['gamename'] == name:
            new_score = {
                attempt: request_data['attempt'],
                score_num: request_data['score_num']

            }
            store['scores'].append(new_score)
            return jsonify(new_score)
        return jsonify({'message': 'store not found'})


#GET /store/<string:name>/item
@app.route('/game/<string:name>/score')
def get_item_in_game(name):
    for game in games:
        if game['name'] == name:
                return jsonify({score: game['score']})
        return jsonify({message : 'games scores not found'})


app.run(port=5000)
