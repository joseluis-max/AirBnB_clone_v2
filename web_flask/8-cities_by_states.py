#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Return list of states """
    data = storage.all("State")
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def teardown_appcontext(exc):
    """ Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
