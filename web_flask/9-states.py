#!/usr/bin/python3
"""
10. States and State
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def end_session(exc):
    """ This function ends the current session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
