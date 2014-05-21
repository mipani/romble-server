import os
import sqlite3
from flask import Flask, g

dir = os.path.dirname(__file__)
DATABASE = os.path.join(dir, 'romble-db.db')

class EntryNotPresentException(Exception):
	pass

class Game(object):
	def __init__(self, id=None, filename=None, title=None, description=None):
		self.id = id
		self.filename = filename
		self.title = title
		self.description = description

class JsonCollection(object):
	def __init__(self, collection=[]):
		self.collection = collection

class RombleDBHelper:
	db = None
	appContext = None
	cursor = None

	def __init__(self, appContext):
		self.appContext = appContext
		
		# Decorate with teardown upon instantiation
		self.close_connection = self.appContext.teardown_appcontext(self.close_connection)
	
	def init_db(self):
		self.db = getattr(g, '_database', None)
		if self.db is None:
			self.db = g._database = sqlite3.connect(DATABASE)
			self.cursor = self.db.cursor()
	
	def get_game_by_id(self, id):
		self.cursor.execute("SELECT * FROM game WHERE id=?", ( id, ) )
		row = self.cursor.fetchone()
		if row is not None:
			return Game( row[0], row[1], row[2], row[3] )
		else:
			raise EntryNotPresentException()
	
	def get_all_games(self):
		game_list = []
		rows = self.cursor.execute("SELECT * FROM game")
		for row in rows:
			game_list.append(Game(row[0], row[1], row[2], row[3]))
		
		return JsonCollection(game_list)
	
	"""
		Query for a game (limit 20, offset 10)
		
		@param {Dict} options	List of options to accompany this query
		May contain: 
			"field": "all", "rom", "desc", "title"
	"""
	def query_games(self, options, query):
		pass
	
	def close_connection(self, exception):
		self.db = getattr(g, '_database', None)
		if self.db is not None:
			self.db.close()
