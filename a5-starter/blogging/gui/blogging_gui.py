import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        # Continue here with your code!
        #Still workshopping title
        self.setWindowTitle("Cool Title")

        #initializing layout
        layout = QVBoxLayout()
        #Setting up main page Log In button
        button = QPushButton("Log in")
        
        button.setCheckable(True)
        button.clicked.connect(self.Log_in_button)

        #Setting up Quit Button 
        button2 = QPushButton("Quit")

        button2.setCheckable(True)
        button2.clicked.connect(self.Quit_Button)
        #testing Qline
        

        #Adding all buttons to layout
        layout.addWidget(button)
        layout.addWidget(button2)

        #Window Settings
        widget = QWidget()
        widget.setLayout(layout)
        self.setFixedSize(QSize(600, 400))
        self.setCentralWidget(widget)

    def Log_in_button(self):
        print("You want to log in :)")

    def Quit_Button(self):
        print("You want to quit :(")


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log in")
        

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
