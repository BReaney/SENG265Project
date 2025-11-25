from blogging.dao.post_dao import PostDAO
import time
from blogging.configuration import Configuration
from blogging.post import Post
from pickle import load, dump
import os


class PostDAOPickle(PostDAO):
    ###configure configuration, toggle persistence, set filename,
    def __init__(self):
        self.configuration = Configuration()
        self.persistence = self.configuration.__class__.autosave
        self.filename = f'{self.configuration.__class__.records_path}/{1111114444}{self.configuration.__class__.records_extension}'
        self.posts = {}
        if self.persistence == True:
            self.load_posts()
        
    ###load the dao posts to the object
    def load_posts(self):
        try:
            with open(self.filename, 'rb') as file:
                self.posts = load(file)
        except:
            pass
    ###write the posts collection to the .dat file
    def dump_posts(self):
        with open(self.filename, 'wb') as file:
            dump(self.posts, file)
    ###return the keyed post else return None
    def search_post(self, key):
        return self.posts.get(key)
        # pass
    
    ### create post, update persistence file, return results of searching the post
    def create_post(self, post):
        self.posts[post.code] = post
        if self.persistence == True:
            self.dump_posts()
        return self.search_post(post.code)
        # pass

    ###iterate through the posts collection and return a list of posts containing the string in their representation
    def retrieve_posts(self, search_string):
        retrieved_posts = []
        for x, y in self.posts.items():
            if search_string in y.__repr__():
                retrieved_posts.append(self.posts.get(x))
        return retrieved_posts
    
    ###if the post is found, update the parameter fields then update the persistence file and return True else return None
    def update_post(self, key, new_title, new_text):
        post = self.search_post(key)
        if post == None:
            return None
        post.set_title(new_title)
        post.set_text(new_text)
        post.set_update(time.time())
        self.posts[key] = post
        if self.persistence == True:
            self.dump_posts()
        return True
    
    ###if the post does not exist, return None; if the post exists, remove it from the collection then update the persistence file and return True
    def delete_post(self, key):
        if self.search_post(key) == None:
            return None
        self.posts.pop(key)
        if self.persistence == True:
            self.dump_posts()
        return True
        # pass
    
    ###return a list of all posts in the post collection 
    def list_posts(self):
        all_posts = []
        for x,y in self.posts.items():
            all_posts.insert(0, self.posts.get(x))
        return all_posts
        # pass