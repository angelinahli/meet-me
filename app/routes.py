import flask
import os
from werkzeug.utils import secure_filename

from app import app
from program.users import *
from program.events import *
from program.parse import schedule
from program_info import info
from forms import LoginForm, SignUpForm, NewEventForm

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
    
    if login.validate_on_submit():
        dbpath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            "static", 
            "user_data.json"
        )
        user_dicts = get_user_dicts(dbpath)
        username = flask.request.form.get("username").lower()
        password = flask.request.form.get("password")

        if not valid_existing_user(username, user_dicts=user_dicts):
            login.username.errors.append("This user doesn't exist!")
        elif not valid_login(username, password, user_dicts=user_dicts):
            login.password.errors.append("This password is invalid!")
        else:
            first_name = user_dicts[username]["first_name"]
            flask.flash("Hi, {}!".format(first_name))
            return flask.redirect(flask.url_for("index"))

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
        username = flask.request.form.get("username").lower() # usernames are case insensitive

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

@app.route("/new_event/", methods=["GET", "POST"])
def new_event():
    new_event = NewEventForm()
    dct = {"title": "Schedule new event", "form": new_event}

    if new_event.validate_on_submit():
        start_time = flask.request.form.get("start_time")
        end_time = flask.request.form.get("end_time")

        if not valid_start_endtime(start_time, end_time):
            new_event.end_time.errors.append("End time must be after start time!")
            return flask.render_template("new_event.html", **dct)
        
        names = flask.request.form.get("usernames")
        if not valid_userlist_length(names):
            new_event.usernames.errors.append("Must provide at least two usernames!")
            return flask.render_template("new_event.html", **dct)

        # don't fetch '''database''' unless everything else is right first
        dbpath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            "static", 
            "user_data.json"
        )
        user_dicts = get_user_dicts(dbpath)
        userlist = get_userlist(names)
        for username in userlist:
            if not valid_existing_user(username, user_dicts=user_dicts):
                msg = "User with username '{}' does not exist!".format(username)
                new_event.usernames.errors.append(msg)
                return flask.render_template("new_event.html", **dct)

        schedule = dict(
            event_name=flask.request.form.get("event_name"),
            start_time=get_datetime(start_time),
            end_time=get_datetime(end_time),
            minutes=int(flask.request.form.get("minutes")),
            usernames=userlist
        )
        return flask.redirect(flask.url_for("possible_times"), **schedule)

    return flask.render_template("new_event.html", **dct)

@app.route("/possible_times/", methods=["GET"])
def possible_times():
    event_name = flask.request.args.get("event_name")
    start_time = flask.request.args.get("start_time")
    end_time = flask.request.args.get("end_time")
    minutes = flask.request.args.get("minutes")

    dbpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "static", 
        "user_data.json"
    )
    usernames = flask.request.args.get("usernames")
    user_dicts = get_user_dicts(dbpath)
    user_list = [User(**user_dicts[username]) for username in usernames]

    times = schedule(start_time, end_time, minutes, user_list)
    
    dct = {
        "title": "Possible Meeting Times for {}".format(event_name),
        "events": times
    }
    return flask.render_template("possible_times.html", **dct)

