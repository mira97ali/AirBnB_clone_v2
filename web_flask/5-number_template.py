#!/usr/bin/python3
"""Is it a number?"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index Page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """C is Fun"""
    return "C " + text.replace("_", " ")


@app.route(
    "/python",
    defaults={"text": "is cool"},
    strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text):
    """Python is Cool"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbersandtemplates(n):
    """Number template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
