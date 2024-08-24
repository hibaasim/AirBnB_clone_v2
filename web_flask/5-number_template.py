#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Return 'n is a number' if it is int"""
    if isinstance(n, int):
        return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """Return html page if n is int"""
    if isinstance(n, int):
        return (render_template("5-number.html", n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
