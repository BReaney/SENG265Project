class Post:
    def __init__(self,c, ti, te, cr, up):
        self.code = c
        self.title = ti
        self.text = te
        self.creation = cr
        self.update = up

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

    def set_code(self, c):
        self.code = c

    def set_title(self, ti):
        self.title = ti

    def set_text(self, te):
        self.text = te

    def set_creation(self, cr):
        self.creation = cr

    def set_update(self, up):
        self.update = up

