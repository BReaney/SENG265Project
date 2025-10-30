import string
from blog import Blog

class Controller:
    #login function, takes a username and a password, returns false if 
    def __init__(self):
        self.username = 'user'
        self.passphrase = 'blogging2025'
        self.loggedin = FALSE

    def login(user, password):
    #login function implementation
        if user == self.username:
            if password == self.passphrase:
                if self.loggedin == FALSE:
                    self.loggedin = TRUE
                    return TRUE
        
        return FALSE

    
    def logout():
    #logout function implementation

