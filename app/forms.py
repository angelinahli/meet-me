from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo

from program_info import info

# helper classes

class DataReqMsg(DataRequired):
    def __init__(self):
        DataRequired.__init__(self, message="Data required.")

class LengthMsg(Length):
    def __init__(self, len_dict, field_name):
        lmin = len_dict["min"]
        lmax = len_dict["max"]
        lmessage = ("Need to provide a {name} between {min} and " + 
            "{max} characters long.").format(
                name=field_name,
                min=lmin,
                max=lmax
        )
        Length.__init__(self, min=lmin, max=lmax, message=lmessage)

# form classes

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataReqMsg()])
    password = PasswordField("Password", validators=[DataReqMsg()])

class SignUpForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataReqMsg()])
    last_name = StringField("Last Name", validators=[DataReqMsg()])
    username = StringField("Username", validators=[
        DataReqMsg(),
        LengthMsg(info["username"], "username")
    ])
    password = PasswordField("Password", validators=[
        DataReqMsg(),
        LengthMsg(info["password"], "password"),
    ])
    confirm = PasswordField("Repeat Password", validators=[
        EqualTo("password", message="Passwords must match.")
    ])

class NewEventForm(FlaskForm):
    start_time = DateTimeField("Start period", validators=[DataReqMsg()])
    end_time = DateTimeField("End period", validators=[DataReqMsg()])
