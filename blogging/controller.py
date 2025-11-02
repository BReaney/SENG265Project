import string
from blogging.blog import Blog

class Controller:
    #login function, takes a username and a password, returns false if wrong credentials or already loggedin
    def __init__(self, username = 'user', passphrase = 'blogging2025'):
        self.username = username
        self.passphrase = passphrase
        self.loggedin = False

    def login(self, username, passphrase):
    #login function implementation
        if username == self.username:
            if passphrase == self.passphrase:
                if self.loggedin == False:
                    self.loggedin = True
                    return True
        return False

    
    def logout(self):
    #logout function implementation
        if self.loggedin == False:
            return False
        self.loggedin = False
        return True
