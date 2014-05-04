#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the very beginning of the Romble project.'

if __name__ == '__main__':
    app.run()
