class Blog:
    """A class that represents a blog"""
    def __init__(self, id, name, url, email):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
    
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

    def set_id(self, num):
        self.id = num

    def set_name(self, n):
        self.id = n

    def set_url(self, u):
        self.url = u

    def set_email(self, e):
        self.email = e
