#!/usr/bin/python3
"""HBNB file"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def function_route():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def function_hbnb():
    """Return HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
