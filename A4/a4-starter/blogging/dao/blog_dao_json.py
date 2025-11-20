class ConcreteBlogDAOJSON(BlogDAO):

    def __init__(self):
        self.filename = "blogging/blogs.json"
        try:
            with open(self.filename, 'rb') as file:
                strin = file.read()
                self.blogs = json.load(file)
        except FileNotFoundError:
            with open(self.filename, 'wb') as file:
                self.blogs = {}
        
    def search_blog(self, key):
        try:
            with open(self.filename, 'rb')as file:
                blogs = json.load
        pass
    
    def create_blog(self, blog):
        with open(self.filename, 'rb') as file:
            json.dump(blog, file)    
        
    def retrieve_blogs(self, search_string):
        pass
    
    def update_blog(self, key, blog):
        pass
    
    def delete_blog(self, key):
        pass
    
    def list_blogs(self):
        pass