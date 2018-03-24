"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""
from datetime import datetime, timedelta
from Parse import parseCal


class User(object):
    def __init__(self, firstName, lastName, email, username, password, link):
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

        if(link[-4:] == ".ics"):
            self.userEvents = parseCal(link)
        else:
            #throw exception?

    # def setUserEvents(self, userEvents):
    #     """
    #     Stores the user's events in an array
    #     """
    #     if(type(userEvents) == type([0, 1, 2, 3, 4])):
    #         events = userEvents
    #     else:
    #         events = []


    def getName(self):
        return(self.firstName + " " + self.lastName)

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def resetFirstName(self, newFirstName):
        self.firstName = newFirstName

    def resetLastName(self, newLastName):
        self.lastName = newLastName

    def resetEmail(self, newEmail):
        self.email = newEmail

    def resetUsername(self, newUsername):
        self.username = newUsername

    def resetPassword(self, newPassword):
        self.password = newPassword
