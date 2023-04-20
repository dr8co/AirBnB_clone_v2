#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0 port 5000
Routes:
    '/hbnb': display HBnB home page
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the main page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
