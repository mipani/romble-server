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

class RombleDBHelper:
	db = None
	appContext = None

	def __init__(self, appContext):
		self.appContext = appContext
		
		# Decorate with teardown upon instantiation
		self.close_connection = self.appContext.teardown_appcontext(self.close_connection)
	
	def init_db(self):
		self.db = getattr(g, '_database', None)
		if self.db is None:
			self.db = g._database = sqlite3.connect(DATABASE)
	
	def get_game_by_id(self, id):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM game WHERE id=?", ( id, ) )
		row = cursor.fetchone()
		if row is not None:
			return Game( row[0], row[1], row[2], row[3] )
		else:
			raise EntryNotPresentException()
	
	def close_connection(self, exception):
		self.db = getattr(g, '_database', None)
		if self.db is not None:
			self.db.close()
