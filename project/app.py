import os
import math
import json

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///moodtracker.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/moodchart")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        #Validate username and password:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("Must choose an username")

        if not password:
            return apology("Must choose a password")

        if not confirmation:
            return apology("Must confirm password")

        if password != confirmation:
            return apology("Your password do not match")

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        except:
           return apology("You already exist!")

        #user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
        #if user_id != " ":
        flash("Successfully registered!")
        return redirect("/")

    else:
         return render_template("/register.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trackmymood", methods=["GET", "POST"])
@login_required
def trackmymood():
    if request.method == "POST":
        #Recognize user:
        user_id = session["user_id"]
        print(user_id)

        pounds = { 'happy': 1, 'normal': 0.5, 'sad': 0.1,
            'good': 1, 'decent': 0.5, 'poor': 0.1,
            'yes': 1, 'medium': 0.5, 'no': 0.1 }

        #Implement the answers into the user's table:
        mood = request.form.get("mood")
        mood_pound = pounds[(mood)]
        print(mood_pound)
        sleep = request.form.get("sleep")
        sleep_pound = pounds[(sleep)]
        print(sleep_pound)
        exercise = request.form.get("exercise")
        exercise_pound = pounds[(exercise)]
        print(exercise_pound)
        eating = request.form.get("eating")
        eating_pound = pounds[(eating)]
        print(eating_pound)

        average = (pounds[(mood)] + pounds[(sleep)] + pounds[(exercise)] + pounds[(eating)]) / 4
        print(average)

        db.execute("INSERT INTO trackmymood (user_id, mood, sleep, exercise, eating, Average) VALUES(?, ?, ?, ?, ?, ?)", user_id, mood_pound, sleep_pound, exercise_pound, eating_pound, average)

        return redirect("/moodchart")

    else:
        return render_template("trackmymood.html")

@app.route("/moodchart", methods=["GET"])
@login_required
def moodchart():
    ##Show graphic of the user's data from trackmymood"""
    #Displays an HTML table for the user currently logged in
    user_id = session["user_id"]
    print(user_id)

    graphicmood = db.execute("SELECT date, mood, sleep, exercise, eating, Average FROM trackmymood WHERE user_id = ?", user_id)
    print(graphicmood)

    return render_template("moodchart.html", graphicmood=graphicmood)