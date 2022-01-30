#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)

data = storage.all()


@app.teardown_appcontext
def teardown_appcontext():
    storage.close()


@app.route('states_list', strict_slashes=False)
def states_list():
    """ Return list of states """
    return render_template('7-states_list.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
