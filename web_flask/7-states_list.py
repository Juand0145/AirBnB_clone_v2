#!/usr/bin/python3
"""List of states file"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Is a methdo display a HTML page"""
    states = []
    for key, value in storage.all(State).items():
        states.append(value)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(response_or_exc):
    """Close the SQL database"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
