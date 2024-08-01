#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a given string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return C <text>"""
    text = text.replace("_", " ")
    return (f"C {text}")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """Return Python <text>"""
    text = text.replace("_", " ")
    return (f"Python {text}")

if __name__ == "__main__":
    app.run(host="0.0.0.0")