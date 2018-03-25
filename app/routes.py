import flask
import os
from werkzeug.utils import secure_filename

from app import app
from program.users import valid_new_user, add_user_db
from program_info import info
from forms import LoginForm, SignUpForm

# db_filepath = flask.url_for("static", filename="user_data.json")

@app.route("/")
@app.route("/index/")
def index():
    dct = {"title": "Meet Me"}
    return flask.render_template("index.html", **dct)

@app.route("/login/", methods=["GET", "POST"])
def login():
    login = LoginForm()
    dct = {"title": "Login", "form": login}
    
    if login.errors:
        print(login.errors)

    if login.validate_on_submit():
        login.username.data
        login.password.data

    # just brand new thing
    return flask.render_template("login.html", **dct)

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    signup = SignUpForm()
    dct = {"title": "Sign Up", "form": signup, "info": info}

    if signup.validate_on_submit():
        # '''database''' dbpath
        dbpath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            "static", 
            "user_data.json")
        username = flask.request.form.get("username")

        if valid_new_user(username=username, filepath=dbpath):
            # deal with grabbing files
            file = flask.request.files["file"]
            filename = username + secure_filename(file.filename)
            userpath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(userpath)

            user_dict = dict(
                first_name=flask.request.form.get("first_name"),
                last_name=flask.request.form.get("last_name"),
                username=username,
                password=flask.request.form.get("password"),
                link=userpath
            )
            add_user_db(dbpath, **user_dict)
            flask.flash("Congrats, you're all set! Please sign in to proceed")
            return flask.redirect(flask.url_for("login"))
        
        else:
            signup.username.errors.append("This username is already taken!")

    return flask.render_template("sign_up.html", **dct)

@app.route("/new_event/", methods=["GET"])
def new_event():
    dct = {"title": "Schedule new event"}
