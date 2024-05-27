from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") ## thats a decorator - a type of function that modifys essentialy another function
def index():
    return render_template("index.html") ## = print to the user's screen

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)

