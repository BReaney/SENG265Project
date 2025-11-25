import json
from blogging.dao.blog_dao import BlogDAO
from blogging.dao.blog_encoder import BlogEncoder
from blogging.dao.blog_decoder import BlogDecoder
from blogging.blog import Blog
from blogging.configuration import Configuration
import os
class ConcreteBlogDAOJSON(BlogDAO):

    def __init__(self):
        self.configuration = Configuration()
        self.autosave = self.configuration.__class__.autosave
        self.filename = "blogging/blogs.json"
        self.blogs = {}
        try:
            #if file exists but is empty, treat as if it doesnt exist.
            if os.stat(self.filename).st_size == 0:
                fp = open(self.filename, 'w')
                fp.close()
            else:    
                #if file exists but has data, continue
                with open(self.filename, 'r') as file:
                    # get a list of all lines in the file, currently json encoded
                    things = file.readlines()
                    #for every line from the file:
                    #1. load the current line, decoding it using the blog_decoder
                    #2. add the blog to the dictionary of blogs, using its id as the key. 
                    for item in things:
                        curblog = json.loads(item,cls=BlogDecoder)
                        self.blogs[curblog.id] = curblog
        #if file isnt found, create file named blogs.json in the blogging directory, open it and close it. 
        except FileNotFoundError:
            fp = open(self.filename, 'w')
            fp.close()
               
    
    ###return the blog from the collection if it exists else return None
    def search_blog(self, key):
        return self.blogs.get(key)
        
    
    ###add the passed blog to the blog collection and update persistent collection
    def create_blog(self, blog):
        
        self.blogs[blog.id] = Blog(blog.id, blog.name, blog.url, blog.email)
        ###update persistent collection if persistence is toggled
        if self.autosave == True:
            with open(self.filename, 'a') as file:
                blog_json = json.dumps(blog, cls=BlogEncoder)
            
                file.write(blog_json)    
                file.write('\n')
    ###retrieve all blogs with the given string in the name field
    def retrieve_blogs(self, search_string):
        r_blogs = []
        for items in self.blogs:
            if search_string in self.blogs[items].name:
                r_blogs.append(self.blogs[items])

        return r_blogs
        
    ###update given blog attributes and update persistence file if toggled, return the search of the blog from the collection
    def update_blog(self, key, blog):
        
        self.blogs[key] = blog
        if self.autosave == True:
            with open(self.filename, 'w') as file:
            
                for items in self.blogs:
                    blog_json = json.dumps(self.blogs[items], cls=BlogEncoder)
                    file.write(blog_json)
                    file.write('\n')

        return self.blogs[key]
        
    ###delete the blog with the given key from the collection if it exists and return True, return False if the blog does not exist
    def delete_blog(self, key):
        if(self.search_blog(key) == None):
            return False
        
        self.blogs.pop(key)
        if self.autosave == True:
            with open(self.filename, 'w') as file:
            
                for items in self.blogs:
                    blog_json = json.dumps(self.blogs[items], cls=BlogEncoder)
                    file.write(blog_json)
                    file.write('\n')
        return True

    ###return a list of all blogs in the collection, built by iterating through the list of keys in the collection
    def list_blogs(self):
        i = list(self.blogs.keys())
        li = []
        for index in range(len(self.blogs)):
            li.append(self.blogs[i[index]])

        return li