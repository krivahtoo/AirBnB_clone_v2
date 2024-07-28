#!/usr/bin/python3
"""
Task 8. List of states
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ This function returns the states from html """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def end_session(exc):
    """ This function ends the current session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
