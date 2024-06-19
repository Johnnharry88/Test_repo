#!/usr/bin/python3
"""Flask App module"""
from flask import Flask, render_template
from equi_model import storage

app = Flask(__name__)


@app.route('/state', strict_slashes=False)
def state():
    states = storage.all(State).values()
    return render_template('0-states.html', states = states)

@app.teardown_appcontext
def teardoen(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
