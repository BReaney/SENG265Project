class blog:
    """A class that represents a blog"""
    def __init__(self, num, n, u, e):
        self.id = num
        self.name = n
        self.url = u
        self.email = e

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_email(self):
        return self.email

