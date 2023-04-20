#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0 port 5000
Routes:
    '/states_list': display an HTML page
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
