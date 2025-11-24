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
from blogging.dao.blog_dao_json import ConcreteBlogDAOJSON
from blogging.configuration import Configuration
from pickle import load, dump
import json
import hashlib
class Controller:
    

    
    def __init__(self):
        self.users = self.load_users()
        self.loggedin = False
        self.blogs_dao = ConcreteBlogDAOJSON()
        self.current_blog = None
        self.configuration = Configuration()
        self.autosave = self.configuration.__class__.autosave
    

    def load_users(self):
        users = {}
        infile = open('blogging/users.txt', 'r')
        
        for lines in infile:
            tok = lines.strip().split(',')
            users[tok[0]] = tok[1]
        infile.close()
        return users
    
        ####################Login/Logout Functions#####################
        #used function from Lab 09 to get the password hash. 
    def get_password_hash(self, password):
        
        encoded_password = password.encode('utf-8')    
        hash_object = hashlib.sha256(encoded_password)      
        hex_dig = hash_object.hexdigest()   

        return hex_dig
    def login(self, username, passphrase):
    #login function, takes a username and a password, returns false if wrong credentials or already loggedin
           
        if self.loggedin == True:
            raise DuplicateLoginException
        
        hashpassword = self.get_password_hash(passphrase)    
        if self.users.get(username) == hashpassword:
            self.loggedin = True
            return True

        raise InvalidLoginException

    
    def logout(self):
    #logout function implementation
        if self.loggedin == False:
            raise InvalidLogoutException
        self.unset_current_blog()
        self.loggedin = False
        return True

##############################Create/Search blog functions#########################

    def create_blog(self, id, name, url, email):
        if self.loggedin == False:
            raise IllegalAccessException
        
        if self.blogs_dao.search_blog(id) != None:
            raise IllegalOperationException
        nblog = Blog(id, name, url, email)   
        self.blogs_dao.create_blog(nblog)
        return self.blogs_dao.search_blog(id)
    
    def search_blog(self, id):
    #id search the blog list
        if self.loggedin == False:
            raise IllegalAccessException
        return self.blogs_dao.search_blog(id)
    
    def retrieve_blogs(self, name):
    #searches the blog list by string and returns a new list of all blogs with titles containing the string
        if self.loggedin != True:
            raise IllegalAccessException
        retrieved_blogs = self.blogs_dao.retrieve_blogs(name)
           
            
        return retrieved_blogs
    
# #######################Update blog functions##########################

    def update_blog(self, cur_id, new_id, new_name, new_url, new_email):
        # pick a blog by id, update blog values.
        if self.loggedin != True:
            raise IllegalAccessException
        if self.blogs_dao.blogs.get(cur_id) == None or (cur_id != new_id and self.blogs_dao.blogs.get(new_id) != None):
            raise IllegalOperationException
        if self.current_blog != None:
            if cur_id == self.current_blog.id:
                raise IllegalOperationException
        nblog = Blog(new_id, new_name, new_url, new_email)
        self.blogs_dao.delete_blog(cur_id)
        self.blogs_dao.update_blog(new_id, nblog)
        return True
    
    ####################Delete Blog Functions####################
    def delete_blog(self, id):
        #delete a blog by id. return False if the blog list is empt, not signed in, or current blog, return None if the blog does not exist, else delete blog and return True
        if self.loggedin != True:
            raise IllegalAccessException
        if len(self.blogs_dao.blogs) == 0 or (self.current_blog != None and id == self.current_blog.id) or self.search_blog(id) == None:
            raise IllegalOperationException
        self.blogs_dao.delete_blog(id)
        return True
    
    
#     ####################list_blogs Functions#####################
    def list_blogs(self):
        #list all blogs
        if self.loggedin != True:
            raise IllegalAccessException
        blogs = self.blogs_dao.list_blogs()
        return blogs
    
    ##################set/get current blog functions#############
    def get_current_blog(self):
        #get current blog, return None if not logged in or does not exist
        if self.loggedin != True:
            raise IllegalAccessException
        return self.current_blog
    
    
    def set_current_blog(self, id):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.search_blog(id) == None:
            raise IllegalOperationException
        self.current_blog = self.search_blog(id)
        return True
    
    def unset_current_blog(self):
        if self.loggedin != True:
            raise IllegalAccessException
        self.current_blog = None
        return

###################create post#########################
    ##create_post: performs validity checks before calling blog.create_post
    def create_post(self, title, text):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        return self.current_blog.create_post(title, text)
    
# ################################################### search post

    # performs validity checks before passing query to blog
    def search_post(self, code):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        return self.current_blog.search_post(code)
    
# #####################################Retrieve posts#####################

    #handle request validity checks, return a call to blog to retrieve a list of posts containing a substring within the title or text
    def retrieve_posts(self, substring):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        return self.current_blog.retrieve_posts(substring)
 ################################### Update Posts ######################
        #takes a code, new info, inserts the new info into the post of key code
    def update_post(self, code, new_title, new_text):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        if self.current_blog.search_post(code) == None:
            return None
        
        a = self.current_blog.search_post(code)
        a.set_title(new_title)
        a.set_text(new_text)
        a.set_update(time.time())
        return True

################################### Delete Posts ########################
        ###Takes a key, and deletes the post with said key.
        ###TODO: once exceptions are handled, replace this implementation with the commented out implementation which passes deletion responsibility to the blog class
        ###TODO: implement exception handling
    # def delete_post(self, key):
    #     if self.current_blog == None:
    #         return None
    #     return self.current_blog.delete_post(key)

    def delete_post(self, key):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        if self.current_blog.search_post(key) == None:
            return None
        # a = self.current_blog
        # a.posts.pop(key)
        # return True
        return self.current_blog.delete_post(key)

    
# ################################### List All Posts of Current Blogs ###########

    def list_posts(self):
        if self.loggedin != True:
            raise IllegalAccessException
        if self.current_blog == None:
            raise NoCurrentBlogException
        # a = []
        # for x in self.current_blog.posts:
        #     a.insert(0, self.current_blog.posts.get(x))
        
            
        # return a    
        return self.current_blog.list_posts()

    
        
        
