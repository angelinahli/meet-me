import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "some-super-duper-secret-key")
    UPLOAD_FOLDER = "app/static/ical_files/"
    MAX_CONTENT_PATH = 100000