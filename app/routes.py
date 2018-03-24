import flask
from app import app

@app.route("/")
@app.route("/index/")
def index():
    dct = {"title": "Meet Me"}
    return flask.render_template("index.html", **dct)