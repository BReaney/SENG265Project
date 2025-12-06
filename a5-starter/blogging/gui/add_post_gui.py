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

        self.layout_grid = QGridLayout()
        self.setLayout(self.layout_grid)

        label_code = QLabel('Code')
        label_title = QLabel('Title')
        label_text = QLabel('Text')
        
        self.text_code = QLineEdit()
        self.text_title = QLineEdit()
        self.text_text = QLineEdit()
        
        button_clear = QPushButton('Clear')
        button_cancel = QPushButton('Cancel')
        button_enter = QPushButton('Enter')

        self.layout_grid.addWidget(label_code, 0, 0)
        self.layout_grid.addWidget(self.text_code, 0, 1)
        self.layout_grid.addWidget(label_title, 1, 0)
        self.layout_grid.addWidget(self.text_title, 1, 1)
        self.layout_grid.addWidget(label_text, 2, 0)
        self.layout_grid.addWidget(self.text_text, 2, 1)
        self.layout_grid.addWidget(button_clear, 3, 0)
        self.layout_grid.addWidget(button_cancel, 3, 1)
        self.layout_grid.addWidget(button_enter, 3, 2)        

        button_clear.clicked.connect(self.clear_button_clicked)
        button_cancel.clicked.connect(self.cancel_button_clicked)
        button_enter.clicked.connect(self.enter_button_clicked)

    def clear_button_clicked():
        pass
    def cancel_button_clicked():
        pass
    def enter_button_clicked():
        pass
