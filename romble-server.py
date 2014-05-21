#!/usr/bin/env python

"""
	romble-server (dev)
	(c) mipani 2014
"""

import json
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from romble_db.RombleDBHelper import RombleDBHelper, Game, EntryNotPresentException

# Basic Setup
app = Flask(__name__)
api = Api(app, catch_all_404s=True)
dbHelper = RombleDBHelper(app)
parser = reqparse.RequestParser()
parser.add_argument('test', type=int)

@app.before_request
def setup_db():
	dbHelper.init_db()

def encode(obj):
	return obj.__dict__

def handle_error(exception):
	return { 'server_error': str(exception) }

class GameEndpoint(Resource):
	"""
		Rest Resource for Game
	"""
	def get(self, game_id):
		try:
			obj = dbHelper.get_game_by_id(game_id)
		except EntryNotPresentException:
			abort(404, message="Game {} does not exist".format(game_id))

		print obj.__dict__
		return json.dumps(obj.__dict__)

class GameCollectionEndpoint(Resource):
	"""
		Rest Resource for Game Collection (broken)
	"""
	def get(self):
		obj = dbHelper.get_all_games()
		print obj.__dict__
		return json.dumps(obj.__dict__, ensure_ascii=True, default=encode)

api.add_resource(GameEndpoint, '/game/<int:game_id>')
api.add_resource(GameCollectionEndpoint, '/game')

# Remove this line when deploying to Apache!
if __name__ == '__main__':
    app.run(debug=True)
