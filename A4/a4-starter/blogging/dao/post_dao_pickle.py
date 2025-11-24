from blogging.dao.post_dao import PostDAO

class PostDAOPickle(PostDAO):

    def __init__(self):
        self.posts = {}
    
    def search_post(self, key):
        return self.posts.get(key)
        # pass
    
    def create_post(self, post):
        self.posts[post.code] = post
        return self.search_post(post.code)
        # pass
    
    def retrieve_posts(self, search_string):
        pass
    
    def update_post(self, key, new_title, new_text):
        pass
    
    def delete_post(self, key):
        pass
    
    def list_posts(self):
        pass