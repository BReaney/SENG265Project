import string
from blogging.blog import Blog
from blogging.blog import Post
import time
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class Controller:
    

    
    def __init__(self, username = 'user', passphrase = '123456'):
        self.username = username
        self.passphrase = passphrase
        self.loggedin = False
        self.blogs = {}
        self.current_blog = None
        self.autosave = False

        ####################Login/Logout Functions#####################

    def login(self, username, passphrase):
    #login function, takes a username and a password, returns false if wrong credentials or already loggedin
        
        if username == self.username:
            if passphrase == self.passphrase:
                if self.loggedin == False:
                    self.loggedin = True
                    return True
        raise InvalidLoginException

    
    def logout(self):
    #logout function implementation
        if self.loggedin == False:
            raise InvalidLogoutException
            
        self.loggedin = False
        self.unset_current_blog()
        return True

##############################Create/Search blog functions#########################

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
    
#######################Update blog functions##########################

    def update_blog(self, cur_id, new_id, new_name, new_url, new_email):
        #pick a blog by id, update blog values.
        if self.loggedin != True or self.blogs.get(cur_id) == None or (cur_id != new_id and self.blogs.get(new_id) != None) or (self.current_blog != None and (cur_id == self.current_blog.id or new_id == self.current_blog.id)):
            return False
        self.blogs.pop(cur_id)
        self.blogs[new_id] = Blog(new_id, new_name, new_url, new_email)
        return True
    
    ####################Delete Blog Functions####################
    def delete_blog(self, id):
        #delete a blog by id. return False if the blog list is empt, not signed in, or current blog, return None if the blog does not exist, else delete blog and return True
        if self.loggedin != True or len(self.blogs) == 0 or (self.current_blog != None and id == self.current_blog.id):
            return False
        if self.blogs.pop(id, None) == None: #removes value AND checks success, None is set as the default return value if no blog is found
            return None
        return True
    
    
    ####################list_blogs Functions#####################
    def list_blogs(self):
        #list all blogs
        if self.loggedin != True:
            return None
        blogs = []
        for i in self.blogs.keys():
            blogs.append(self.blogs.get(i))
        return blogs
    
    ##################set/get current blog functions#############
    def get_current_blog(self):
        #get current blog, return None if not logged in or does not exist
        if self.loggedin != True:
            return None
        return self.current_blog
    
    
    def set_current_blog(self, id):
        if self.loggedin != True or self.search_blog(id) == None:
            return False
        self.current_blog = self.search_blog(id)
        return True
    
    def unset_current_blog(self):
        self.current_blog = None
        return

###################create post#########################
    ##create_post: performs validity checks before calling blog.create_post
    def create_post(self, title, text):
        if self.loggedin != True or self.current_blog == None:
            return None
        return self.current_blog.create_post(title, text)
    
################################################### search post

    # performs validity checks before passing query to blog
    def search_post(self, code):
        if self.loggedin != True or self.current_blog == None:
            return None
        return self.current_blog.search_post(code)
    
#####################################Retrieve Blog#####################

    #handle request validity checks, return a call to blog to retrieve a list of posts containing a substring within the title or text
    def retrieve_posts(self, substring):
        if self.loggedin != True or self.current_blog == None:
            return None
        return self.current_blog.retrieve_posts(substring)
 ################################### Update Posts ######################
        #takes a code, new info, inserts the new info into the post of key code
    def update_post(self, code, new_title, new_text):
        if self.current_blog == None:
            return None
        if self.current_blog.search_post(code) == None:
            return None
        
        a = self.current_blog.search_post(code)
        a.set_title(new_title)
        a.set_text(new_text)
        a.set_update(time.time())
        return True

################################### Delete Posts ########################
        #Takes a key, and deletes the post with said key.
    def delete_post(self, key):
        if self.current_blog == None:
            return None
        if self.current_blog.search_post(key) == None:
            return None
        a = self.current_blog
        a.posts.pop(key)
        return True
    
################################### List All Posts of Current Blogs ###########

    def list_posts(self):
        if self.current_blog == None:
            return None
        if self.loggedin != True:
            return None
        a = []
        for x in self.current_blog.posts:
            a.insert(0, self.current_blog.posts.get(x))
        
            
        return a    