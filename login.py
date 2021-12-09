from PyQt5 import QtWidgets,uic
from menu import main_window 
from user import User

class Login_window(QtWidgets.QMainWindow):
    def __init__(self, user):
        self.user = user 
        super(Login_window, self).__init__() 
        uic.loadUi('login.ui', self) 
        self.login_button.clicked.connect(self.login)
        self.login_button_2.clicked.connect(self.signup)
        self.show() 
    def login(self):
        username=self.username_edit.text()
        password=self.password_edit_2.text()
        user1=User(username,password)
        if user1.login():
            self.cams = main_window() 
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
        
    def deneme():
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Login_window('User')
    app.exec_()