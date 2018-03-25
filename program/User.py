"""
This class is meant to store the user information like the user's name,
username, email, and events so that it could be used to compare schedules and
find free time with other users
"""
from datetime import *
from Parse import parseCal


class User(object):
    def __init__(self, firstName, lastName, username, password, link, start, end, email=None):
        
        self.firstName = firstName if type(firstName) == type("") else "User's"
        self.lastName = lastName if type(lastName) == type("") else "Name"
        self.email = email
        self.username = username
        self.password = password

        link = link.strip()
        if(link[-4:] == ".ics"):
            self.link = link
            self.events = parseCal(link)

        self.start = start #start and end should already be datetime objects
        self.end = end

    def getName(self):
        return(self.firstName + " " + self.lastName)

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getEvents(self):
        return self.events

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

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
