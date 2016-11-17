from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {
        'gamename': 'anglegame',
        'scores': [
            {
                'attempt': 4,
                'score_num': 98
            }

        ]
    },
    {
        'gamename' : 'circlegame',
        'scores': []
    }

]

# GET /game --- TO SEE ALL THE GAMES
@app.route('/games')
def get_games():
    return jsonify({'games': games}) #converts the games into json. But we need the json to be an object so we are making our games array the value of a key. {games: games}


# GET /game/<string: gamename> --- SHOW A SPECIFIC GAME
@app.route('/games/<string:gamename>') # stringname specfic to flask:means some name can be filled in
def get_game(gamename):
    for game in games:
        if game['gamename'] ==  gamename:
            return jsonify(game)
        return jsonify({message : 'game not found'})


#GET /game/<string:gamename>/scores --- SHOW SCORES FROM A GAME
@app.route('/games/<string:gamename>/scores')
def get_item_in_game(gamename):
    for game in games:
        if game['gamename'] == gamename:
            return jsonify({scores: game['scores']})
        return jsonify({message : 'games scores not found'})


# POST /game data: {gamename: } -- TO ADD A NEW GAME TO THE DATA
@app.route('/game', methods=['POST'])
def create_game():
    request_data = request.get_json()
    new_game = {
        'name' : request_data['gamaname'],
        scores: []
    }
    games.append(new_game)
    return jsonify(new_game)


# POST /game/<string: gamename>/score -- TO ADD A NEW SCORE TO A GAME
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



app.run(port=5000)
