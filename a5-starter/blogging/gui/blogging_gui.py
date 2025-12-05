import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from blogging.controller import Controller
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
# from login_gui import LoginGUI

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        # Continue here with your code!
        #Still workshopping title
        self.controller = Controller()
        self.setWindowTitle("Main Menu")
        self.resize(600, 400)
        self.layout_page = QStackedLayout()
        #initializing login layout
        layout_start_page = QVBoxLayout()
        #Setting up main page Log In button
        button_login_page = QPushButton("Log in")
        
        
        button_login_page.clicked.connect(self.login_page_button_clicked)

        #Setting up Quit Button 
        button_quit = QPushButton("Quit")

      
        button_quit.clicked.connect(self.quit_button_clicked)
        #testing Qline
        

        #Adding all buttons to layout
        layout_start_page.addWidget(button_login_page)
        layout_start_page.addWidget(button_quit)

        #Window Settings
        start_page_widget = QWidget()
        start_page_widget.setLayout(layout_start_page)
        self.layout_page.addWidget(start_page_widget)
        self.layout_page.setCurrentIndex(0)
        
        self.page_widget = QWidget()
        self.page_widget.setLayout(self.layout_page)
        self.setFixedSize(QSize(600, 400))
        self.setCentralWidget(self.page_widget)

        ################ Add Login Page #####################
        # self.login_gui = LoginGUI(self.controller)
        # layout_login_page = QGridLayout()
         #### define textbox layout #######
        layout_login_input = QGridLayout()
        

        ##### text box definition and labeling #######
        label_user = QLabel("Username")
        self.text_user = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()

        ##### add text boxes to layout ###########
        layout_login_input.addWidget(label_user, 0, 0)
        layout_login_input.addWidget(self.text_user, 0, 1)
        layout_login_input.addWidget(label_password, 1, 0)
        layout_login_input.addWidget(self.text_password, 1, 1)

        ################# define login button layout ###############
        layout_login_buttons = QHBoxLayout()

        #### button config ####
        button_login = QPushButton("Log in")
        button_clear = QPushButton("Clear")
        button_cancel = QPushButton("Cancel")

        button_login.setEnabled(True)
        button_clear.setEnabled(True)
        button_cancel.setEnabled(True)

        layout_login_buttons.addWidget(button_login)
        layout_login_buttons.addWidget(button_clear)
        layout_login_buttons.addWidget(button_cancel)

        ### connect button signals to slots ###
        button_login.clicked.connect(self.login_button_clicked)
        button_clear.clicked.connect(self.clear_button_clicked)
        button_cancel.clicked.connect(self.cancel_button_clicked)

        ###### widget layout config #############

        layout_login_page = QVBoxLayout()

        login_input_widget = QWidget()
        login_input_widget.setLayout(layout_login_input)
        login_buttons_widget = QWidget()
        login_buttons_widget.setLayout(layout_login_buttons)
        layout_login_page.addWidget(login_input_widget)
        layout_login_page.addWidget(login_buttons_widget)
        login_page_widget = QWidget()
        login_page_widget.setLayout(layout_login_page)
        self.layout_page.addWidget(login_page_widget)
        # widget.setLayout(layout_login_page)

        # self.setCentralWidget(widget)

        ######################## Add Home Page ########################
        layout_home_page = QVBoxLayout()
        layout_home_menu = QVBoxLayout()

        home_page_widget = QWidget()

        home_menu_widget = QWidget()

        button_add_new_blog = QPushButton('Add New Blog')
        button_search_blog_by_id = QPushButton('Search Blog By ID')
        button_retrieve_blogs_by_name = QPushButton('Retrieve Blogs By Name')
        button_change_blog_data = QPushButton('Change Blog Data')
        button_remove_blog = QPushButton('Remove Blog')
        button_list_all_blogs = QPushButton('List All Blogs')
        button_edit_blog = QPushButton('Edit Blog')
        button_log_out = QPushButton('Log Out')

        layout_home_menu.addWidget(button_add_new_blog) 
        layout_home_menu.addWidget(button_search_blog_by_id) 
        layout_home_menu.addWidget(button_retrieve_blogs_by_name) 
        layout_home_menu.addWidget(button_change_blog_data) 
        layout_home_menu.addWidget(button_remove_blog)
        layout_home_menu.addWidget(button_list_all_blogs) 
        layout_home_menu.addWidget(button_edit_blog)
        layout_home_menu.addWidget(button_log_out)

        button_add_new_blog.clicked.connect(self.add_new_blog_button_clicked) 
        button_search_blog_by_id.clicked.connect(self.search_blog_by_id_button_clicked) 
        button_retrieve_blogs_by_name.clicked.connect(self.retrieve_blogs_by_name_button_clicked) 
        button_change_blog_data.clicked.connect(self.change_blog_data_button_clicked) 
        button_remove_blog.clicked.connect(self.remove_blog_button_clicked)
        button_list_all_blogs.clicked.connect(self.list_all_blogs_button_clicked) 
        button_edit_blog.clicked.connect(self.edit_blog_button_clicked)
        button_log_out.clicked.connect(self.log_out_button_clicked)

        home_menu_widget.setLayout(layout_home_menu)
        layout_home_page.addWidget(home_menu_widget)
        home_page_widget.setLayout(layout_home_page)
        self.layout_page.addWidget(home_page_widget)

                #################### Create Add Blog Window ##################
        add_blog_layout = QGridLayout()
        add_blog_widget = QWidget()

        #################### Create Labels and Lines for all Fields################

        label_id = QLabel("ID")
        self.text_id = QLineEdit()
        label_name = QLabel("Name")
        self.text_name = QLineEdit()
        label_url = QLabel("Url")
        self.text_url = QLineEdit()
        label_email = QLabel("Email")
        self.text_email = QLineEdit()


        ################### Organize layouts ######################

        add_blog_layout.addWidget(label_id, 0, 0)
        add_blog_layout.addWidget(self.text_id, 0, 1)

        add_blog_layout.addWidget(label_name, 1, 0)
        add_blog_layout.addWidget(self.text_name, 1, 1)

        add_blog_layout.addWidget(label_url, 2, 0)
        add_blog_layout.addWidget(self.text_url, 2, 1)

        add_blog_layout.addWidget(label_email, 3, 0)
        add_blog_layout.addWidget(self.text_email, 3, 1)

        ################### Complete/Clear/Cancel Buttons ################
        button_layout = QHBoxLayout()
        self.add_blog_complete_button = QPushButton("Complete")
        self.add_blog_clear_button = QPushButton("Clear")
        self.add_blog_cancel_button = QPushButton("Cancel")

        self.add_blog_complete_button.setEnabled(True)
        self.add_blog_clear_button.setEnabled(True)
        self.add_blog_cancel_button.setEnabled(True)

        button_layout.addWidget(self.add_blog_complete_button)
        button_layout.addWidget(self.add_blog_clear_button)
        button_layout.addWidget(self.add_blog_cancel_button)

        self.add_blog_cancel_button.clicked.connect(self.add_blog_cancel_button_clicked)
        self.add_blog_complete_button.clicked.connect(self.add_blog_complete_button_clicked)
        self.add_blog_clear_button.clicked.connect(self.add_blog_clear_button_clicked)
        ################### Add Blog Page Layout ###############
        add_blog_page_layout = QVBoxLayout()

        add_blog_top_widget = QWidget()
        add_blog_top_widget.setLayout(add_blog_layout)
        add_blog_bottom_widget = QWidget()
        add_blog_bottom_widget.setLayout(button_layout)
        add_blog_page_layout.addWidget(add_blog_top_widget)
        add_blog_page_layout.addWidget(add_blog_bottom_widget)
        add_blog_widget.setLayout(add_blog_page_layout)
        self.layout_page.addWidget(add_blog_widget)

        
        ####################Search Blog Window #################
        search_blog_layout = QGridLayout()
        search_blog_widget = QWidget()

        ####################Search Bar Label ##############

        label_search_blog = QLabel("Search for blog by ID")
        self.blog_search_id_text = QLineEdit()

        search_blog_layout.addWidget(label_search_blog, 0, 0)
        search_blog_layout.addWidget(self.blog_search_id_text, 0, 1)

        ################### Search/Quit Button #################

        search_blog_button_layout = QHBoxLayout()

        self.search_blog_search_button = QPushButton("Search")
        self.search_blog_quit_button = QPushButton("Quit")

        self.search_blog_search_button.setEnabled(True)
        self.search_blog_quit_button.setEnabled(True)

        search_blog_button_layout.addWidget(self.search_blog_search_button)
        search_blog_button_layout.addWidget(self.search_blog_quit_button)

        self.search_blog_search_button.clicked.connect(self.search_blog_search_button_clicked)
        self.search_blog_quit_button.clicked.connect(self.search_blog_quit_button_clicked)

        #################### Create the Search Blog page #########################

        search_blog_page_layout = QVBoxLayout()

        search_blog_top_widget = QWidget()
        search_blog_top_widget.setLayout(search_blog_layout)

        search_blog_bottom_widget = QWidget()
        search_blog_bottom_widget.setLayout(search_blog_button_layout)

        search_blog_page_layout.addWidget(search_blog_top_widget)
        search_blog_page_layout.addWidget(search_blog_bottom_widget)

        search_blog_widget.setLayout(search_blog_page_layout)
        self.layout_page.addWidget(search_blog_widget)



        ########################### Search Blog by Name #######################

        layout_search_blog_name = QGridLayout()
        search_blog_name_widget = QWidget()

        ########################### Search Bar #######################

        label_search_blog_name = QLabel("Search by name")
        self.search_blog_name = QLineEdit()

        layout_search_blog_name.addWidget(label_search_blog_name, 0, 0)
        layout_search_blog_name.addWidget(self.search_blog_name, 0, 1)

        ########################## Search/Quit Button #####################

        layout_search_blog_name_button = QHBoxLayout()

        self.search_blog_name_search_button = QPushButton("Search")
        self.search_blog_name_quit_button = QPushButton("Quit")

        self.search_blog_name_search_button.setEnabled(True)
        self.search_blog_name_quit_button.setEnabled(True)

        layout_search_blog_name_button.addWidget(self.search_blog_name_search_button)
        layout_search_blog_name_button.addWidget(self.search_blog_name_quit_button)

        self.search_blog_name_search_button.clicked.connect(self.search_blog_name_search_button_clicked)
        self.search_blog_name_quit_button.clicked.connect(self.search_blog_name_quit_button_clicked)

        ############################## Create Search by name page #######################
        

        search_blog_name_page_layout = QVBoxLayout()

        search_blog_name_top_widget = QWidget()
        search_blog_name_top_widget.setLayout(layout_search_blog_name)

        search_blog_name_bottom_widget = QWidget()
        search_blog_name_bottom_widget.setLayout(layout_search_blog_name_button)

        search_blog_name_page_layout.addWidget(search_blog_name_top_widget)
        search_blog_name_page_layout.addWidget(search_blog_name_bottom_widget)

        search_blog_name_widget.setLayout(search_blog_name_page_layout)
        self.layout_page.addWidget(search_blog_name_widget)

    def toggle_window(self, window):
        self.layout_page.setCurrentIndex(window)
        self.page_widget.setLayout(self.layout_page)
        self.setCentralWidget(self.page_widget)

    def login_page_button_clicked(self):
        # QMessageBox.information(self, 'Login', 'You want to log in :)')
        # self.login_gui.show()
        self.toggle_window(1)
        
        pass

    def quit_button_clicked(self):
        # QMessageBox.information(self, 'Quit', 'You want to quit :(')
        self.close()

    def login_button_clicked(self):
        try:
            self.login()
            button = QMessageBox.information(self, 'Success', 'Login successful')
            if button == QMessageBox.StandardButton.Ok:
                self.toggle_window(2)
        except:
            button = QMessageBox.warning(self, 'Failure', 'Login failed')
            if button == QMessageBox.StandardButton.Ok:
                self.clear_button_clicked()

        pass

    def clear_button_clicked(self):
        self.text_password.setText('')
        self.text_user.setText('')

    def cancel_button_clicked(self):
        # self.close()
        
            self.toggle_window(0)
        
        
    
    def add_new_blog_button_clicked(self):
        self.toggle_window(3)
        pass
    def search_blog_by_id_button_clicked(self):
        self.toggle_window(4)
        pass
    def retrieve_blogs_by_name_button_clicked(self):
        self.toggle_window(5)
        pass
    def change_blog_data_button_clicked(self):
        pass
    def remove_blog_button_clicked(self):
        pass
    def list_all_blogs_button_clicked(self):
        pass
    def edit_blog_button_clicked(self):
        pass
    def log_out_button_clicked(self):
        self.log_out()
        self.toggle_window(0)
        pass
    def login(self):
        user = self.text_user.text()
        password = self.text_password.text()
        self.controller.login(user, password)
        pass
    def log_out(self):
        self.controller.logout()
    
    
    
    ############################ Add Blog Functions ##############################
    def add_blog_complete_button_clicked(self):

        self.add_blog()
        button = QMessageBox.information(self, "Added Blog Successfully!", "Success!")
        if button == QMessageBox.StandardButton.Ok:
            self.toggle_window(2)
        

    def add_blog_clear_button_clicked(self):
        self.text_email.setText("")
        self.text_id.setText("")
        self.text_name.setText("")
        self.text_url.setText("")
        

    def add_blog(self):
        id = int(self.text_id.text())
        name = self.text_name.text()
        email = self.text_name.text()
        url = self.text_url.text()
        self.controller.create_blog(id, name, url, email)

    def add_blog_cancel_button_clicked(self):
        self.toggle_window(2)



    ############################### Search Blog Functions #############################
    def search_blog_quit_button_clicked(self):
        self.toggle_window(2)
    

    def search_blog_search_button_clicked(self):
        self.blog_search_id_text.setText("")
        self.search_blog()

    def search_blog(self):
        try:


            dialog_layout = QVBoxLayout()

            searchid = int(self.blog_search_id_text.text())

            found_blog = self.controller.search_blog(searchid)

            dialog = QDialog(self)
            dialog.setWindowTitle("Found your blog!")

            label_message = QLabel(f'ID: {found_blog.id}\nNAME: {found_blog.name} \nURL: {found_blog.url} \nEmail: {found_blog.email}')
            dialog_layout.addWidget(label_message)
            dialog.setFixedSize(500, 500)
            dialog.setLayout(dialog_layout)
            button = dialog.exec()
            
            

            
        except:

            button = QMessageBox.warning(self, "Error", "Blog could not be found :(")
            if button == QMessageBox.StandardButton.Ok:
                self.blog_search_id_text.setText("")
                self.toggle_window(2)

        ########################## Search Blog by name functions ############################3
    def search_blog_name_quit_button_clicked(self):
        self.search_blog_name.setText("")
        self.toggle_window(2)

    def search_blog_name_search_button_clicked(self):
        self.search_blog_by_name()

    def search_blog_by_name(self):
        try:


            dialog_layout = QVBoxLayout()

            search_string = self.search_blog_name.text()

            found_blogs = self.controller.retrieve_blogs(search_string)

            dialog = QDialog(self)
            dialog.setWindowTitle("Found your blog!")
            for results in found_blogs:
                label_message = QLabel(f'ID: {results.id}\nNAME: {results.name} \nURL: {results.url} \nEmail: {results.email}')
                dialog_layout.addWidget(label_message)

            dialog.setFixedSize(500, 500)
            dialog.setLayout(dialog_layout)
            button = dialog.exec()
            
            

            
        except:

            button = QMessageBox.warning(self, "Error", "Blog could not be found :(")
            if button == QMessageBox.StandardButton.Ok:
                self.search_blog_name.setText("")
                self.toggle_window(2)

# class LoginGUI(QMainWindow):
#     def __init__(self, controller):
#         super().__init__()
#         self.controller = controller
#         self.setWindowTitle("Login")

#         ################# define textbox layout ####################
#         layout1 = QGridLayout()
        

#         ##### text box definition and labeling #######
#         label_user = QLabel("Username")
#         self.text_user = QLineEdit()
#         label_password = QLabel("Password")
#         self.text_password = QLineEdit()

#         ##### add text boxes to layout ###########
#         layout1.addWidget(label_user, 0, 0)
#         layout1.addWidget(self.text_user, 0, 1)
#         layout1.addWidget(label_password, 1, 0)
#         layout1.addWidget(self.text_password, 1, 1)

#         ################# define login button layout ###############
#         layout2 = QHBoxLayout()

#         #### button config ####
#         self.button_login = QPushButton("Log in")
#         self.button_clear = QPushButton("Clear")
#         self.button_cancel = QPushButton("Cancel")

#         self.button_login.setEnabled(True)
#         self.button_clear.setEnabled(True)
#         self.button_cancel.setEnabled(True)

#         layout2.addWidget(self.button_login)
#         layout2.addWidget(self.button_clear)
#         layout2.addWidget(self.button_cancel)

#         ### connect button signals to slots ###
#         self.button_login.clicked.connect(self.login_button_clicked)
#         self.button_clear.clicked.connect(self.clear_button_clicked)
#         self.button_cancel.clicked.connect(self.cancel_button_clicked)

#         ####################### widget layout config ##############################

#         layout3 = QVBoxLayout()

#         top_widget = QWidget()
#         top_widget.setLayout(layout1)
#         bottom_widget = QWidget()
#         bottom_widget.setLayout(layout2)
#         layout3.addWidget(top_widget)
#         layout3.addWidget(bottom_widget)
#         widget = QWidget()
#         widget.setLayout(layout3)

#         self.setCentralWidget(widget)

    # def login_button_clicked(self):
    #     try:
    #         self.login()
    #         button = QMessageBox.information(self, 'Success', 'Login successful')
    #         if button == QMessageBox.StandardButton.Ok:
    #             self.cancel_button_clicked()
    #     except:
    #         button = QMessageBox.warning(self, 'Failure', 'Login failed')
    #         if button == QMessageBox.StandardButton.Ok:
    #             self.clear_button_clicked()

    #     pass
    # def clear_button_clicked(self):
    #     self.text_password.setText('')
    #     self.text_user.setText('')

    # def cancel_button_clicked(self):
    #     self.close()
    #     pass
    # def login(self):
    #     user = self.text_user.text()
    #     password = self.text_password.text()
    #     self.controller.login(user, password)
    #     pass


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log in")

# class AddBlogGUI(QMainWindow):
#     def __init__(self, controller):
#         super.__init__()
#         self.controller = controller
#         self.setWindowTitle("Add a Blog")       

#         #################### Create the Grid Layout ##################
#         add_blog_layout = QGridLayout()


#         #################### Create Labels and Lines for all Fields################

#         label_id = QLabel("ID")
#         self.text_id = QLineEdit()
#         label_name = QLabel("Name")
#         self.text_name = QLineEdit()
#         label_url = QLabel("Url")
#         self.text_url = QLineEdit()
#         label_email = QLabel("Email")
#         self.text_email = QLineEdit


#         ################### Organize layouts ######################

#         add_blog_layout.addWidget(label_id, 0, 0)
#         add_blog_layout.addWidget(self.text_id, 0, 1)

#         add_blog_layout.addWidget(label_name, 1, 0)
#         add_blog_layout.addWidget(self.text_name, 1, 1)

#         add_blog_layout.addWidget(label_url, 2, 0)
#         add_blog_layout.addWidget(self.text_url, 2, 1)

#         add_blog_layout.addWidget(label_email, 3, 0)
#         add_blog_layout.addWidget(self.text_email, 3, 1)

#         ################### Complete/Clear/Cancel Buttons ################
#         button_layout = QHBoxLayout()
#         self.complete_button = QPushButton()
#         self.clear_button = QPushButton()
#         self.cancel_button = QPushButton()

#         self.complete_button.setEnabled(True)
#         self.clear_button.setEnabled(True)
#         self.cancel_button.setEnabled(True)

#         button_layout.addWidget(self.complete_button)
#         button_layout.addWidget(self.clear_button)
#         button_layout.addWidget(self.cancel_button)

#         ################### Page Layout ###############
#         page_layout = QVBoxLayout()

#         top_widget = QWidget()
#         top_widget.setLayout(add_blog_layout)
#         bottom_widget = QWidget()
#         bottom_widget.setLayout(button_layout)
#         page_layout.addWidget(top_widget)
#         page_layout.addWidget(bottom_widget)
#         widget = QWidget()
#         widget.setLayout(page_layout)


def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
