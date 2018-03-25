"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""
import simplejson

from datetime import *
from parse import parse_cal

# helper functions to communicate with json """"database"""" (fix later)

def get_user_dicts(filepath):
    with open(filepath, "rb") as fl:
        all_text = fl.read()
    return simplejson.loads(all_text)

def valid_new_user(username, filepath=None, user_dicts=None):
    assert filepath or user_dicts
    all_user_dicts = user_dicts if user_dicts else get_user_dicts(filepath)
    return username not in all_user_dicts

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

# user related objects

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
            print link

    def get_name(self):
        return(self.first_name + " " + self.last_name)

class Users(object):

    def __init__(self, filepath):
        self.all_users = dict()
        user_dicts = get_user_dicts(filepath)
        for user, dct in user_dicts.items():
            new_user = User(
                first_name=dct.get("first_name"),
                last_name=dct.get("last_name"),
                username=user,
                password=dct.get("password"),
                link=dct.get("link"),
            )
            self.all_users[user] = new_user

    def check_valid_user(self, username, password):
        # get method won't throw an exception
        user = self.all_users.get(username)
        if not user:
            return False
        return user.password == password

    def get_user(self, username):
        return self.all_users.get(username) # returns none if none exists

if __name__ == "__main__":
    fp = "../app/static/user_data.json"
    # add_user_db(fp, "Angie", "Li", "ali6", "sth", "abc", start=None, end=None)
    # for dct in get_user_dicts(fp).values():
    #     print dct
    # users = Users(fp)
    # for user in users.all_users.values():
    #     print user.password
    pass
    