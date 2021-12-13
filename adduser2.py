from PyQt5 import QtWidgets,uic
from adduser1 import User

class Login_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_window, self).__init__() 
        uic.loadUi('ui/login.ui', self) 
        self.login_button_2.clicked.connect(self.signup)
        self.show()

    def signup(self):
        username = self.username_edit.text()
        password = self.password_edit_2.text()
        user = User(username,password)
        if user.control_username():
            user.signup()
            QtWidgets.QMessageBox.about(self,'Your Information!','User name: {} - Password: {}'.format(username,password))
        else:
            QtWidgets.QMessageBox.about(self,'Username already exists!','{} username is already used by someone!'.format(username))