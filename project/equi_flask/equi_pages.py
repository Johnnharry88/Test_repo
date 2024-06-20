#!/usr/bin/python3
from flask import Flask, render_template
from os import environ
from equi_model import storage
app = Flask(__name__)


@app.teardown_appcontext
def clsoe_db(error):
    storage.close()


@app.route('/', strict_slashes=False)
def home():
    """Serves the landing page of Eui site"""
    return render_template('Equi_page.html')


@app.route('/login', strict_slashes=False)
def login():
    """Serves the login page of Equi site"""
    return render_template("Equi_Login.html")


@app.route('/signup', strict_slashes=False)
def signup():
    """Serves the sign up pages"""
    return render_template("Equi_userform.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
