import sqlite3
from flask import Flask, g

DATABASE = 'romble-db.db'

class RombleDBHelper:
	db = None
	appContext = None

	def __init__(self, appContext):
		self.appContext = appContext
		
		# Decorate with teardown upon instantiation
		self.close_connection = self.appContext.teardown_appcontext(self.close_connection)

	def test(self):
		print self.db
		return str(self.db)
	
	def init_db(self):
		self.db = getattr(g, '_database', None)
		if self.db is None:
			self.db = g._database = sqlite3.connect(DATABASE)
	
	def close_connection(self, exception):
		self.db = getattr(g, '_database', None)
		if self.db is not None:
			self.db.close()
