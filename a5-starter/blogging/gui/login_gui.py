import sys
from blogging_gui import BloggingGUI
from blogging.configuration import Configuration
from blogging.controller import Controller
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton

class LoginGUI(QMainWindow):
    def __init__(self, controller, parent):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.setWindowTitle("Login")

        layout1 = QVBoxLayout()
        login_button = QPushButton("Log in")
        cancel_button = QPushButton("Cancel")


        label_user = QLabel("Username")
        self.text_user = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()

        login_button.clicked.connect(self.login_button_clicked)

    def login_button_clicked(self):
        pass
    def cancel_button_clicked(self):
        pass
    def login(self):
        pass