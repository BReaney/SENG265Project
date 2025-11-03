import string
from blogging.blog import Blog

class Controller:
    

    
    def __init__(self, username = 'user', passphrase = 'blogging2025'):
        self.username = username
        self.passphrase = passphrase
        self.loggedin = False
        self.blogs = {}

        ####################Login/Logout Functions#####################

    def login(self, username, passphrase):
    #login function, takes a username and a password, returns false if wrong credentials or already loggedin
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

##############################Create/Search blog functions#########################

    def create_blog(self, id, name, url, email):
        if self.loggedin == False or self.blogs.get(id) == False:
            return None
        self.blogs |= {id : Blog(id, name, url, email)}
        return self.blogs.get(id)
