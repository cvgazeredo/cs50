from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Football",
    "Volleyball",
    "Soccer"
]


@app.route("/")
def index(): ## its he function that will get called for this particular route
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    #Validate the submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    #Confirm registration
    return render_template("success.html")