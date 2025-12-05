import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from blogging.controller import Controller

class PostingGUI(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.layout_stack = QStackedLayout()
        layout_blog_menu = QVBoxLayout()
        blog_menu_widget = QWidget()
        blog_menu_widget.setLayout(layout_blog_menu)
        self.layout_stack.addWidget(blog_menu_widget)
        self.setLayout(self.layout_stack)

        ############### Blog Menu ####################
        button_add_post_to_blog = QPushButton('Add post to blog')
        button_retrieve_posts_from_blog_by_text = QPushButton('Retrieve posts from blog by text')
        button_change_post_from_blog = QPushButton('Change post from blog')
        button_remove_post_from_blog = QPushButton('Remove post from blog')
        button_list_full_blog_contents = QPushButton('List full blog contents')
        button_finish_editing_blog = QPushButton('Finish editing blog')    

        layout_blog_menu.addWidget(button_add_post_to_blog)
        layout_blog_menu.addWidget(button_retrieve_posts_from_blog_by_text)
        layout_blog_menu.addWidget(button_change_post_from_blog)
        layout_blog_menu.addWidget(button_remove_post_from_blog)
        layout_blog_menu.addWidget(button_list_full_blog_contents)
        layout_blog_menu.addWidget(button_finish_editing_blog)    

        button_add_post_to_blog.clicked.connect(self.add_post_to_blog_button_clicked)
        button_retrieve_posts_from_blog_by_text.clicked.connect(self.retrieve_posts_from_blog_by_text_button_clicked)
        button_change_post_from_blog.clicked.connect(self.change_post_from_blog_button_clicked)
        button_remove_post_from_blog.clicked.connect(self.remove_post_from_blog_button_clicked)
        button_list_full_blog_contents.clicked.connect(self.list_full_blog_contents_button_clicked)
        button_finish_editing_blog.clicked.connect(self.finish_editing_blog_button_clicked)    
        
    def add_post_to_blog_button_clicked(self):
        pass
    def retrieve_posts_from_blog_by_text_button_clicked(self):
        pass
    def change_post_from_blog_button_clicked(self):
        pass
    def remove_post_from_blog_button_clicked(self):
        pass
    def list_full_blog_contents_button_clicked(self):
        pass
    def finish_editing_blog_button_clicked(self):
        pass
