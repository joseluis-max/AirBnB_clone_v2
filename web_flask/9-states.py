#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ Return list of states """
    data = storage.all("State")
    return render_template('7-states_list.html', state=data)


@app.route('/states/<id>', strict_slashes=False)
def states_list(id):
    """ Return list of states """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", data=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exc):
    """ Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
