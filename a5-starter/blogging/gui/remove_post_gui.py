import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtWidgets import QPlainTextEdit
from blogging.controller import Controller

class RemovePostGUI(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.layout_grid = QGridLayout()
        self.setLayout(self.layout_grid)

        label_blog_code = QLabel('Blog Code')
        
        self.text_blog_code = QLineEdit()
        
        button_clear = QPushButton('Clear')
        button_cancel = QPushButton('Cancel')
        button_enter = QPushButton('Enter')

        self.layout_grid.addWidget(label_blog_code, 0, 0)
        self.layout_grid.addWidget(self.text_blog_code, 0, 1)
        self.layout_grid.addWidget(button_clear, 1, 0)
        self.layout_grid.addWidget(button_cancel, 1, 1)
        self.layout_grid.addWidget(button_enter, 1, 2)        

        button_clear.clicked.connect(self.clear_button_clicked)
        button_cancel.clicked.connect(self.cancel_button_clicked)
        button_enter.clicked.connect(self.enter_button_clicked)

    def clear_button_clicked(self):
        self.text_blog_code.setText('')
        pass

    def cancel_button_clicked(self):
        self.clear_button_clicked()
        self.parent.toggle_window(1)
        pass

    def enter_button_clicked(self):
        blog_code = int(self.text_blog_code.text())

        try: 
            status = self.controller.delete_post(blog_code)
            layout_dialog = QVBoxLayout()
            text = QPlainTextEdit()
            dialog = QDialog(self)
            dialog.setWindowTitle('Post Deletion Status')
            text.appendPlainText(f'Post {blog_code}\nReturn {status}\n')
            layout_dialog.addWidget(text)
            dialog.setFixedSize(500, 500)
            dialog.setLayout(layout_dialog)
            button = dialog.exec()
            self.clear_button_clicked()

        except: 
            button = QMessageBox.warning(self, 'Error', 'Removal Exception')
            if button == QMessageBox.StandardButton.Ok:
                self.clear_button_clicked()
        pass
