#!/usr/bin/python3
from flask import Flask, render_template, request, session
from flask import url_for, redirect
from os import environ
from equi_model import storage
from equi_model.user import User
from hashlib import md5
app = Flask(__name__)


@app.teardown_appcontext
def clsoe_db(error):
    storage.close()


@app.route('/', strict_slashes=False)
def home():
    """Serves the landing page of Eui site"""
    return render_template('Equi_page.html')


@app.route('/login', methods=["GET", "POST"], strict_slashes=False)
def login():
    """Serves the login page of Equi site"""
    if request.method == "POST":
        username = request.form['email']
        password = request.form['password']
        user = storage.all(User).values()
        for u in user:
            if u.email == username and u.password == password:
                return " You have Logged in successfully"
        return (redirect(url_for("signup")))
    return render_template("Equi_Login.html")


@app.route('/signup', methods=["GET", "POST"], strict_slashes=False)
def signup():
    """Serves the sign up pages"""
    if request.method == "POST":
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        email = request.form['email']
        password = request.form['passwd']
        phone_no = request.form['phone_no']
        gender = request.form['gender']
        address = request.form['address']
        state = request.form['state']
        city = request.form['city']
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password
        user.phone_no = phone_no
        user.gender = gender
        user.address = address
        user.state = state
        user.city = city
        user.save()
        return (redirect(url_for('login')))
    return render_template("Equi_userform.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
