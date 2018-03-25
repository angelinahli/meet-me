from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

from program_info import info

# helper functions

def get_length_v(len_dict, field_name):
    """
    Given a dictionary of min and max lengths, as well as the name of 
    the field we want the length validator for, will return a Length() validator
    """
    min_len = len_dict["min"]
    max_len = len_dict["max"]
    msg = "Need to provide a {name} between {min} and {max} characters long.".format(
        name=field_name,
        min=min_len,
        max=max_len
    )

    return Length(
        min=min_len,
        max=max_len,
        message=msg
    )


# classes

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(message="Data required.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="Data required.")
    ])
    submit = SubmitField("Sign in")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(message="Data required."),
        get_length_v(info["username"], "username")
    ])
    password = PasswordField("New Password", validators=[
        DataRequired(message="Data required."),
        get_length_v(info["password"], "password"),
        EqualTo("confirm", message="Passwords must match.")
    ])
    confirm = PasswordField("Repeat Password")

class NewEventForm(FlaskForm):
    pass