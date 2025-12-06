import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from blogging.controller import Controller

class AddPostGUI(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent