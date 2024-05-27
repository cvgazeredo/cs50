import os
import math

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #Displays an HTML table for the user currently logged in
    user_id = session["user_id"]
    print(user_id)
    # Which stocks the user owns,
    # the numbers of shares owned,
    transactions = db.execute("SELECT symbol, SUM(shares) AS totalShares, price FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    print(transactions)

    current_balance = {}
    for i in range (len(transactions)):
        current_balance[i] = lookup(transactions[i]["symbol"])
    print(current_balance)

    for i in range(len(transactions)):
        current_balance[i]["total"] = transactions[i]["totalShares"] * current_balance[i]["price"]
    print(current_balance)

    user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    user_cash = user_cash_db[0]["cash"]

    return render_template("index.html", transactions=transactions, user_cash=user_cash, current_balance=current_balance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    else:
        #Require that a user input a stock’s symbol
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        print(symbol)
        if not symbol:
            return apology("Must give a symbol")

        #Require that a user input a number of shares

        shares = request.form.get("shares")
        if not shares.isdigit():
            return apology("Must give an interger")

        shares = int(shares)

        print(shares)
        if shares < 0 :
            return apology("Must give a positive interger")

        #Look up a stock’s current price.
        stock = lookup(symbol.upper())
        print(stock)
        if stock == None:
            return apology("No symbol found")
        stock_price = stock["price"]
        print(stock_price)

        #Select how much cash the user currently has
        user_id = session["user_id"]
        print(user_id)
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        print(user_cash_db)
        user_cash = user_cash_db[0]["cash"]
        print(user_cash)

        transaction = shares * stock_price
        print(transaction)
        if user_cash < transaction:
            return apology("You dont have enough money for this transaction")

        #Update the user's cash after the transition
        current_cash = user_cash - transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash, user_id)


        #Keep track of the transactions
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, type) VALUES(?, ?, ?, ?, ?)", user_id, symbol, shares, stock_price, 'true')

        flash("Bought!")
        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    #For each row, make clear whether a stock was bought or sold and include the stock’s symbol,
    # the (purchase or sale) price, the number of shares bought or sold,
    # and the date and time at which the transaction occurred.
    user_id = session["user_id"]
    print(user_id)
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    print(transactions)

    return render_template("history.html", transactions=transactions)

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
        return redirect("/")

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must give a symbol")
        stock = lookup(symbol.upper())
        print(stock)

        if stock == None:
            return apology("No symbol found")

        return render_template("quoted.html", name = stock["name"], price = stock["price"], symbol = stock["symbol"])


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
        return redirect("/")

    else:
        return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        #Show stocks owned by the user:
        transactions = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ? AND type ='true' ", user_id)
        print(transactions)

        #Require that a user input a stock’s symbol.
        #implemented as a select menu whose name is symbol
        symbol = request.form.get("symbol")
        print(symbol)
        #Render an apology if the user fails to select a stock
        #or if (somehow, once submitted) the user does not own any shares of that stock.
        if not symbol:
            return apology("Must select a stock symbol")

        #Require that a user input a number of shares,
        #implemented as a field whose name is shares
        shares = int(request.form.get("shares"))
        print(shares)
        #Render an apology if the input is not a positive integer
        #or if the user does not own that many shares of the stock.
        if not shares:
            return apology("Must select a number")
        if shares <= 0:
            return apology("Must input a positive intereger")

        user_shares_db = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)
        print(user_shares_db)
        user_shares = sum(d['shares'] for d in user_shares_db)
        print(user_shares)
        if shares > user_shares:
            return apology("You dont have enough shares to sell")

        #See current price of the chosen stock to sell:
        stock_price_symbol = lookup(symbol)
        print(stock_price_symbol)
        stock_price = stock_price_symbol["price"]
        print(stock_price)

        #Total value of the transaction:
        sell_transaction = stock_price * shares
        print(sell_transaction)

        #Update the user's cash after the sell transition
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        print(user_cash_db)
        user_cash = user_cash_db[0]["cash"]
        print(user_cash)

        current_cash = user_cash + sell_transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash, user_id)

        #Keep track of the transactions
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, type) VALUES(?, ?, ?, ?, ?)", user_id, symbol, -shares, stock_price, 'false' )

        flash("Sold!")
        return redirect("/")

    else:
        user_id = session["user_id"]
        transactions = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", user_id)
        print(transactions)

        return render_template("sell.html", transactions=transactions)

#Add money in the account
@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():

    if request.method == "GET":
        return render_template("cash.html")

    else:
        cash = int(request.form.get("cash"))
        if not cash:
            return apology("Must give a value")
        if cash < 0:
            return apology("Must give a positive interger")
        print(cash)

        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        print(user_cash_db)
        user_cash = user_cash_db[0]["cash"]
        print(user_cash)

        current_cash = user_cash + cash
        print(current_cash)

        #Update the user's cash after
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash, user_id)

        return render_template("cash.html")