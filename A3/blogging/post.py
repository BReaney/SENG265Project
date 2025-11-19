import time
import string


class Post:
    def __init__(self,code, title, text, creation = time.time(), update = time.time()):
        self.code = code
        self.title = title
        self.text = text
        self.creation = creation
        self.update = update

    def get_code(self):
        return self.code
    
    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_creation(self):
        return self.creation

    def get_update(self):
        return self.update

    def set_code(self, code):
        self.code = code

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_creation(self, creation):
        self.creation = creation

    def set_update(self, update):
        self.update = update

###############################

    def __repr__(self):
        return "Post(%r, %r, %r, %0.7r, %0.7r)" % (self.code, self.title, self.text, self.creation, self.update)


    def __eq__(self, other):
        return self.__repr__() == other.__repr__()