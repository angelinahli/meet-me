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

        self.start = strptime(start) #should convert string to datetime object
        self.end = strptime(end)

    def getName(self):
        return(self.firstName + " " + self.lastName)
