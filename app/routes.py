import flask
from app import app
from forms import LoginForm, SignUpForm

@app.route("/")
@app.route("/index/")
def index():
    dct = {"title": "Meet Me"}
    return flask.render_template("index.html", **dct)

@app.route("/login/")
def login():
    login = LoginForm()
    dct = {"title": "Login", "form": login}
    return flask.render_template("login.html", **dct)