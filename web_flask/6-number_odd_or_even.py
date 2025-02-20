#!/usr/bin/python3
"""Bash script that starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display 'C' followed by the value of text,
    with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Display 'Python' followed by the value of text,
    with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """Display 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page only if n is an integer and show if it is odd or even."""
    odd_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == '__main__':
    """Starts the Flask web application."""
    app.run(host='0.0.0.0', port=5000)
