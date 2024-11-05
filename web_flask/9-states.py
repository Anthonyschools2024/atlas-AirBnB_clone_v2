#!/usr/bin/python3
"""Starts a Flask web application to display a list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


""" routes to requests"""
@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display list of states or cities of a state """
    """ retrieve data from storage"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    if id:
        state = next((state for state in states if state.id == id), None)
        """ render the 9-states.html file """
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-states.html', state=state, cities=cities)
        else:
            return render_template('9-states.html', state=None)
    return render_template('9-states.html', states=states)


""" clos session each time"""
@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
