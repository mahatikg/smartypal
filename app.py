from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {
        gamename: 'anglegame',
        scores: []
    }


]

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




# GET /game/<string: gamename>
@app.route('/game/<string:name>') # stringname specfic to flask:means some name can be filled in
def get_game(name):
    for game in games:
        if store['name'] ==  name:
            return jsonify(game)
        return jsonify({message : 'game not found'})




# GET /game (All)
@app.route('/game')
def get_games():
    return jsonify({'games': games}) #converts the games into json. But we need the json to be an object so we are making our games array the value of a key. {games: games}



# POST /game/<string: gamename>/score to add a new scores to a game's scores
@app.route('/game/<string:name>/score', methods=['POST'])
def create_item_in_game(name):
    request_data = request.get_json()
    for game in games:
        if game['name'] == name:
            new_score = {
                attempt: request_data['attempt'],
                score_num: request_data['score_num']

            }
            store['scores'].append(new_score)



#GET /store/<string:name>/item
@app.route('/game/<string:name>/score')
def get_item_in_game(name):
    for game in games:
        if game['name'] == name:
                return jsonify({score: game['score']})
        return jsonify({message : 'game's scores not found'})


app.run(port=5000)
