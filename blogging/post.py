class Post:
    def __init__(self,code, time, text, creation, update):
        self.code = code
        self.title = time
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

    def set_title(self, time):
        self.title = time

    def set_text(self, text):
        self.text = text

    def set_creation(self, creation):
        self.creation = creation

    def set_update(self, update):
        self.update = update

