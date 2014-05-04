#!/usr/bin/env python
from flask import Flask
from romble_db.RombleDBHelper import RombleDBHelper
app = Flask(__name__)
dbHelper = RombleDBHelper(app)

@app.route('/')
def hello_world():
    return 'This is the very beginning of the Romble project.'

@app.route('/test')
def test():
	dbHelper.init_db()
	return dbHelper.test()

if __name__ == '__main__':
    app.run(debug=True)
