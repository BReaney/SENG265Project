import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtWidgets import QPlainTextEdit
from blogging.controller import Controller

class RetrievePostGUI(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.layout_grid = QGridLayout()
        self.setLayout(self.layout_grid)

        label_title = QLabel('Title')
        
        self.text_title = QLineEdit()
        
        button_clear = QPushButton('Clear')
        button_cancel = QPushButton('Cancel')
        button_enter = QPushButton('Enter')

        self.layout_grid.addWidget(label_title, 0, 0)
        self.layout_grid.addWidget(self.text_title, 0, 1)
        self.layout_grid.addWidget(button_clear, 1, 0)
        self.layout_grid.addWidget(button_cancel, 1, 1)
        self.layout_grid.addWidget(button_enter, 1, 2)        

        button_clear.clicked.connect(self.clear_button_clicked)
        button_cancel.clicked.connect(self.cancel_button_clicked)
        button_enter.clicked.connect(self.enter_button_clicked)

    def clear_button_clicked(self):
        self.text_title.setText('')
        pass

    def cancel_button_clicked(self):
        self.clear_button_clicked()
        self.parent.toggle_window(1)
        pass

    def enter_button_clicked(self):
        title = self.text_title.text()

        try: 
            posts = self.controller.retrieve_posts(title)
            layout_dialog = QVBoxLayout()
            text_list = QPlainTextEdit()
            dialog = QDialog(self)
            dialog.setWindowTitle('Posts Retrieved')
            for i in posts:
                text_list.appendPlainText(f'Code {i.code}\nTitle {i.title}\nText: {i.text}\nCreation {i.creation}\nUpdate {i.update}\n')
                layout_dialog.addWidget(text_list)
            dialog.setFixedSize(500, 500)
            dialog.setLayout(layout_dialog)
            button = dialog.exec()

        except: 
            button = QMessageBox.warning(self, 'Error', 'Retrieval Exception')
            if button == QMessageBox.StandardButton.Ok:
                self.clear_button_clicked()
        pass
