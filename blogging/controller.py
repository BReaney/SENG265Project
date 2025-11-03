import string
from blogging.blog import Blog

class Controller:
    

    
    def __init__(self, username = 'user', passphrase = 'blogging2025'):
        self.username = username
        self.passphrase = passphrase
        self.loggedin = False
        self.blogs = {}

        ####################Login/Logout case Functions#####################

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

##############################Create/Search blog case functions#########################

    def create_blog(self, id, name, url, email):
        if self.loggedin == False or self.blogs.get(id)!= None:
            return None
        self.blogs |= {id : Blog(id, name, url, email)}
        return self.blogs.get(id)
    
    def search_blog(self, id):
    #id search the blog list
        return self.blogs.get(id)
    
    def retrieve_blogs(self, name):
    #searches the blog list by string and returns a new list of all blogs with titles containing the string
        if self.loggedin != True:
            return None
        retrieved_blogs = []
        for x, y in self.blogs.items():     #.items returns the key and the value of each dict entry as x and y respectively
            if name in y.name:              #'in' checks a string for a substring and returns a boolean 
                retrieved_blogs.append(y)   #x:id y:blog
        return retrieved_blogs
    
#######################Update blog case functions##########################

    def update_blog(self, cur_id, new_id, new_name, new_url, new_email):
        #pick a blog by id, update blog values.
        if self.loggedin != True or self.blogs.get(cur_id) == None or (cur_id != new_id and self.blogs.get(new_id) != None):
            return False
        self.blogs.pop(cur_id)
        self.blogs[new_id] = Blog(new_id, new_name, new_url, new_email)
        return True