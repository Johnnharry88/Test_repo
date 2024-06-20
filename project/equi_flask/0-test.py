#!/usr/bin/python3
from flask import Flask, render_template
from equi_model import storage
from equi_model.state import State
from equi_model.city import City
from os import environ

app = Flask(__name__)


@app.route("/state", strict_slashes=False)
def state():
    state = storage.all(State).values()
    city = storage.all(City).values()
       
    return render_template('0-state.html', state_1=state,
            city=city)


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
