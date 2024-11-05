#!/usr/bin/python3
"""Starts a Flask web application to display filters for states and amenities"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with filters for states and amenities"""
    """ retrieve states from storage """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    """ retrieve amenities from storage """
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    """ render the 10-hbnb_filters.html file """
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

""" closes session each time """
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

""" run app on port 5000"""
""" on mac I have to change this to 50000 to test """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
