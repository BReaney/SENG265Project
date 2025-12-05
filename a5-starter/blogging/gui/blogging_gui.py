import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from blogging.controller import Controller
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
        
        button_login_page.setCheckable(True)
        button_login_page.clicked.connect(self.login_page_button_clicked)

        #Setting up Quit Button 
        button_quit = QPushButton("Quit")

        button_quit.setCheckable(True)
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
        pass
    def login(self):
        user = self.text_user.text()
        password = self.text_password.text()
        self.controller.login(user, password)
        pass

class LoginGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Login")

        ################# define textbox layout ####################
        layout1 = QGridLayout()
        

        ##### text box definition and labeling #######
        label_user = QLabel("Username")
        self.text_user = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()

        ##### add text boxes to layout ###########
        layout1.addWidget(label_user, 0, 0)
        layout1.addWidget(self.text_user, 0, 1)
        layout1.addWidget(label_password, 1, 0)
        layout1.addWidget(self.text_password, 1, 1)

        ################# define login button layout ###############
        layout2 = QHBoxLayout()

        #### button config ####
        self.button_login = QPushButton("Log in")
        self.button_clear = QPushButton("Clear")
        self.button_cancel = QPushButton("Cancel")

        self.button_login.setEnabled(True)
        self.button_clear.setEnabled(True)
        self.button_cancel.setEnabled(True)

        layout2.addWidget(self.button_login)
        layout2.addWidget(self.button_clear)
        layout2.addWidget(self.button_cancel)

        ### connect button signals to slots ###
        self.button_login.clicked.connect(self.login_button_clicked)
        self.button_clear.clicked.connect(self.clear_button_clicked)
        self.button_cancel.clicked.connect(self.cancel_button_clicked)

        ####################### widget layout config ##############################

        layout3 = QVBoxLayout()

        top_widget = QWidget()
        top_widget.setLayout(layout1)
        bottom_widget = QWidget()
        bottom_widget.setLayout(layout2)
        layout3.addWidget(top_widget)
        layout3.addWidget(bottom_widget)
        widget = QWidget()
        widget.setLayout(layout3)

        self.setCentralWidget(widget)

    def login_button_clicked(self):
        try:
            self.login()
            button = QMessageBox.information(self, 'Success', 'Login successful')
            if button == QMessageBox.StandardButton.Ok:
                self.cancel_button_clicked()
        except:
            button = QMessageBox.warning(self, 'Failure', 'Login failed')
            if button == QMessageBox.StandardButton.Ok:
                self.clear_button_clicked()

        pass
    def clear_button_clicked(self):
        self.text_password.setText('')
        self.text_user.setText('')

    def cancel_button_clicked(self):
        self.close()
        pass
    def login(self):
        user = self.text_user.text()
        password = self.text_password.text()
        self.controller.login(user, password)
        pass


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
