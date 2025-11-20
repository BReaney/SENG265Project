import json
from blogging.dao.blog_dao import BlogDAO
from blogging.dao.blog_encoder import BlogEncoder
from blogging.dao.blog_decoder import BlogDecoder
from blogging.blog import Blog
import os
class ConcreteBlogDAOJSON(BlogDAO):

    def __init__(self):
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
               
    
    
    def search_blog(self, key):
        return self.blogs.get(key)
        
      
    
    def create_blog(self, blog):
        self.blogs[blog.id] = Blog(blog.id, blog.name, blog.url, blog.email)
        with open(self.filename, 'a') as file:
            blog_json = json.dumps(blog, cls=BlogEncoder)
            
            file.write(blog_json)    
            file.write('\n')
    def retrieve_blogs(self, search_string):
        r_blogs = []
        for items in self.blogs:
            if search_string in self.blogs[items].name:
                r_blogs.append(self.blogs[items])

        return r_blogs
        
    
    def update_blog(self, key, blog):
        pass
    
    def delete_blog(self, key):
        pass
    
    def list_blogs(self):
        pass