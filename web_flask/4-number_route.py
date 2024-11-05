#!/usr/bin/python3
""" init file for flask"""
from flask import Flask

""" create flask app """
app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ return C and value of text """
    return "C " + text.replace('_', ' ')
    """ replace _ with space"""


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ return Python followed by text """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return nis a number if n is an int """
    return f"{n} is a number"


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
