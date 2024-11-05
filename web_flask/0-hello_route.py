#!/usr/bin/python3
""" init file for flask"""
from flask import Flask

""" create flask app """
app = Flask(__name__)


""" route"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return hello HBNB """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
