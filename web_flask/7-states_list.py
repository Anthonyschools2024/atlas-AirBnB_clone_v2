#!/usr/bin/python3
""" Starts a flask web app that returns a greeting """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ function that returns greeting """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that returns a hbnb message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ function that return message, but with a C """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<hiss>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def parseltongue(hiss="is cool"):
    """ function that returnsss a python message """
    return 'Python {}'.format(hiss.replace('_', ' '))


@app.route('/number/<input>', strict_slashes=False)
def digis(input):
    """ function that displays a number if it is an integer """
    if input.isdigit():
        return '{} is a number'.format(input)


@app.route('/number_template/<int:input>', strict_slashes=False)
def html_template(input):
    """ function that displays a HTML page only if input is an integer """
    return render_template('5-number.html', number=input)


@app.route('/number_odd_or_even/<int:input>', strict_slashes=False)
def its_so_odd(input):
    """ function that displays an HTML page that checks odd or even """
    if input % 2 == 0:
        input = '{} is even'.format(input)
    else:
        input = '{} is odd'.format(input)
    return render_template('6-number_odd_or_even.html', can_you_even=input)


@app.route('/states_list', strict_slashes=False)
def show_the_states():
    """ function that displays a HTML page that displays all states created """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ removes current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)