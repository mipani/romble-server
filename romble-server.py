#!/usr/bin/env python

"""
	romble-server (dev)
	(c) mipani 2014
"""

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from romble_db.RombleDBHelper import RombleDBHelper, Game, EntryNotPresentException

# Basic Setup
app = Flask(__name__)
api = Api(app)
dbHelper = RombleDBHelper(app)
parser = reqparse.RequestParser()
parser.add_argument('test', type=int)

@app.before_request
def setup_db():
	dbHelper.init_db()

class GameEndpoint(Resource):
	"""
		Rest Resource for Game
	"""
	def get(self, game_id):
		try:
			game = dbHelper.get_game_by_id(game_id)
		except EntryNotPresentException:
			abort(404, message="Game {} does not exist".format(game_id))
		
		return game.__dict__

api.add_resource(GameEndpoint, '/game/<int:game_id>')

# Remove this line when deploying to Apache!
if __name__ == '__main__':
    app.run(debug=True)
