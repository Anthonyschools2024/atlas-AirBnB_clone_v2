#!/usr/bin/python3
"""Starts a Flask web application to display a list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-states_list.html', states=states)
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
