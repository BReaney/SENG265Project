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