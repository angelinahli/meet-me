import os

class Config(object):
    curr_path = os.path.dirname(os.path.realpath(__file__))

    SECRET_KEY = os.environ.get("SECRET_KEY", "some-super-duper-secret-key")
    UPLOAD_FOLDER = os.path.join(curr_path, "tmp", "ical_files")
    MAX_CONTENT_PATH = 100000