from flask import Flask

app = Flask(__name__)
games = [
    {
        gamename: 'anglegame',
        score: []
    }
    {
        gamename: 'circlegame'
        score: []
    }
]

# POST /game data: {gamename: }
@app.route('/game', methods=['POST'])
def create_game():
    'should create game data?'



# GET /game/<string: gamename>
@app.route('/game/<string:name>') # the stringname situation is specfic to flask because it means that some name can be filled in
def get_game(name):
    pass



# GET /game (All)
@app.route('/game/')
def get_games():
    pass



# POST /game/<string: gamename>/item
@app.route('/game/<string:name>/item', methods=['POST'])
def create_item_in_game(name):
    pass


#GET /store/<string:name>/item
@app.route('/game/<string:name>/item')
def get_item_in_game(name):
    pass


app.run(port=5000)
