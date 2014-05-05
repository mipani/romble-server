#!/usr/bin/env python

from flask import Flask
from romble_db.RombleDBHelper import RombleDBHelper, Game

app = Flask(__name__)
dbHelper = RombleDBHelper(app)

@app.before_request
def setup_db():
	dbHelper.init_db()

@app.route('/')
def hello_world():
    return 'This is the very beginning of the Romble project.'

# Used only for very cursory testing!
@app.route('/test')
def test():
	game = dbHelper.get_game_by_id(1)
	return str(game.id) + ' ' + game.filename + ' ' + game.title + ' ' + game.description

if __name__ == '__main__':
    app.run(debug=True)
