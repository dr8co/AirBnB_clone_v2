#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0 port 5000
Routes:
    '/states': display an HTML page with a list of all states
    '/states/<id>': display an HTML page with the id of the state
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays an HTML page"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays an HTML page with information about <id>, if it exists"""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
