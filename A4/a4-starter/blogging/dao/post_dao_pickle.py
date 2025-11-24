from blogging.dao.post_dao import PostDAO
import time
from blogging.configuration import Configuration
from blogging.post import Post
from pickle import load, dump
import os

class PostDAOPickle(PostDAO):

    def __init__(self):
        self.configuration = Configuration()
        self.persistence = self.configuration.__class__.autosave
        self.filename = f'{self.configuration.__class__.records_path}/{1111114444}{self.configuration.__class__.records_extension}'
        self.posts = {}
        self.load_posts()

    def load_posts(self):
        try:
            with open(self.filename, 'rb') as file:
                self.posts = load(file)
        except:
            pass

    def dump_posts(self):
        with open(self.filename, 'wb') as file:
            dump(self.posts, file)

    def search_post(self, key):
        return self.posts.get(key)
        # pass
    
    def create_post(self, post):
        self.posts[post.code] = post
        if self.persistence == True:
            self.dump_posts()
        return self.search_post(post.code)
        # pass
    
    def retrieve_posts(self, search_string):
        retrieved_posts = []
        for x, y in self.posts.items():
            if search_string in y.__repr__():
                retrieved_posts.append(self.posts.get(x))
        return retrieved_posts
    
    def update_post(self, key, new_title, new_text):
        pass
    
    def delete_post(self, key):
        if self.search_post(key) == None:
            return None
        self.posts.pop(key)
        return True
        # pass
    
    def list_posts(self):
        all_posts = []
        for x,y in self.posts.items():
            all_posts.insert(0, self.posts.get(x))
        return all_posts
        # pass