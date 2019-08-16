"""
This file simply defines a User class for creation of User objects in gamertags.py.
"""

#define user object
class User:
    def getGamertag(self):
        return self.gamertag

    def getID(self):
        return self.id

    def getHostID(self):
        return self.hostid

    def getPopularity(self):
        return self.popularity

    def __init__(self, gamertag, id, hostid):
        self.gamertag = gamertag
        self.id = id
        self.hostid = hostid
        self.popularity = 0