import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

lm = LoginManager()
lm.init_app(app)
curr_path = os.path.dirname(os.path.realpath(__file__))
oid = OpenID(app, os.path.join(curr_path, "tmp"))

from app import routes