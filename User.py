"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""

name = "User"
username = ""
email = ""
events = []

class User(object):
    def __init__(self, name, username, email):
        if(type(name) == type("")):
            self.name = name

        if(type(username) == type("")):
            self.username = username

        if(type(email) == type("")):
            self.email = email

    def user_events(userEvents):
        """
        Stores the user's events in an array
        """
        if(type(userEvents) == type([0, 1, 2, 3, 4])):
            events = userEvents
        else:
            events = []

