from blogging.post import Post
class Blog:
    """A class that represents a blog"""
    def __init__(self, id, name, url, email):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
        self.posts = {}
        self.code = 0
    
    def __repr__(self):
        return "Blog(%d, %r, %r, %r)" % (self.id, self.name, self.url, self.email)

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            return True
        else: 
            return False

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_email(self):
        return self.email

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_url(self, url):
        self.url = url

    def set_email(self, email):
        self.email = email

####################################

    def create_post(self, title, text):
        self.code += 1
        self.posts |= {self.code : Post(self.code, title, text)}
        return self.posts[self.code]