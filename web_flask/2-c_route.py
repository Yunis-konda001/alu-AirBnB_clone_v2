#!/usr/bin/python3
"""Bash script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display HBNB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display "C <text>" with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
