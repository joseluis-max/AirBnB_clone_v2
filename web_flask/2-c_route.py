#!/usr/bin/python3
""" C is fun """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Route home return Hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route hbnb return hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
