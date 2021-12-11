from PyQt5 import QtWidgets,uic
import menu
from user import User
import credentials 

class Login_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_window, self).__init__() 
        uic.loadUi('ui/login.ui', self) 
        self.login_button.clicked.connect(self.login)
        self.login_button_2.clicked.connect(self.signup)
        self.credentials.clicked.connect(self.credential_window)
        self.show() 
    def login(self):
        username=self.username_edit.text()
        password=self.password_edit_2.text()
        user1=User(username,password)
        if user1.login():
            self.cams = menu.menu_window(username,password) 
            self.cams.show() 
            self.close()
        else:
            QtWidgets.QMessageBox.about(self,'Invalid!','User name or Password is incorrect!')
            self.password_edit_2.clear()
    def signup(self):
        username=self.username_edit.text()
        password=self.password_edit_2.text()
        user1=User(username,password)
        if user1.control_username():
            user1.signup()
            QtWidgets.QMessageBox.about(self,'Your Information!','User name: {} - Password: {}'.format(username,password))
        else:
            QtWidgets.QMessageBox.about(self,'Username already exists!','{} username is already used by someone!'.format(username))
    def credential_window(self):
        self.cams=credentials.credentials_window()
        self.cams.show()
        self.close()