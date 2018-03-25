"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""
import simplejson

from datetime import *
from parse import parse_cal

# helper functions

def get_user_dicts(filepath):
    with open(filepath, "rb") as fl:
        all_text = fl.read()
    return simplejson.loads(all_text)

def valid_new_user(username, filepath=None, user_dicts=None):
    assert filepath or (user_dicts != None)
    all_user_dicts = user_dicts if user_dicts != None else get_user_dicts(filepath)
    return username not in all_user_dicts

def valid_existing_user(username, filepath=None, user_dicts=None):
    return not valid_new_user(username, filepath=filepath, user_dicts=user_dicts)

def valid_login(username, password, filepath=None, user_dicts=None):
    assert filepath or (user_dicts != None)
    all_user_dicts = user_dicts if user_dicts != None else get_user_dicts(filepath)
    return all_user_dicts[username]["password"] == password

def add_user_db(filepath, first_name, last_name, username, password, link):
    all_user_dicts = get_user_dicts(filepath)
    all_user_dicts[username] = dict(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        link=link,
    )
    with open(filepath, "wb") as fl:
        simplejson.dump(all_user_dicts, fl)
    print "Added user", username

def valid_userlist_length(usernames):
    """Checks whether or not there are at least two usernames in list"""
    return len(usernames.split(",")) >= 2

def get_userlist(usernames):
    return [username.strip().lower() for username in usernames.split(",")]

# user object

class User(object):
    def __init__(self, first_name, last_name, username, password, link):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

        link = link.strip()
        if(link[-4:] == ".ics"):
            self.link = link
            self.events = parse_cal(link)
        
        else:
            print "failed link:", link

    def get_name(self):
        return self.first_name + " " + self.last_name

if __name__ == "__main__":
    fp = "../app/static/user_data.json"
    # add_user_db(fp, "Angie", "Li", "ali6", "sth", "abc", start=None, end=None)
    # for dct in get_user_dicts(fp).values():
    #     print dct
    # users = Users(fp)
    # for user in users.all_users.values():
    #     print user.password
    pass
    