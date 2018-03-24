"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""

class User(object):
    def __init__(self, firstName, lastName, email, username, password):
        if(type(firstName) == type("")):
            self.firstName = firstName
        else:
            self.firstName = "User's"

        if(type(lastName) == type("")):
            self.lastName = lastName
        else:
            self.lastName = "Name"

        if(type(email) == type("")):
            self.email = email

        if(type(username) == type("")):
            self.username = username

        if(type(password) == type("")):
            self.password = password

    def setUserEvents(self, userEvents):
        """
        Stores the user's events in an array
        """
        if(type(userEvents) == type([0, 1, 2, 3, 4])):
            events = userEvents
        else:
            events = []

    def updateEvents(self, moreEvents):
        userEvents += moreEvents

    def getName(self):
        print(self.name)

    def getEmail(self):
        print(self.email)

    def getUsername(self):
        print(self.username)

    def getPassword(self):
        print(self.password)

    def reset
