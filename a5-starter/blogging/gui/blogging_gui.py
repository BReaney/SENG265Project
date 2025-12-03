import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        # Continue here with your code!
        self.setWindowTitle("Cool Title")
        button = QPushButton("Log in")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(600, 400))

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
