from PyQt5 import QtWidgets,uic
from menu import Main_window 
import sys
import os
import json

class Menuscreen_window(QtWidgets.QMainWindow):
    def __init__(self, username=" ",password=" ",time=0,progress=0):
        self.login(username,password,time,progress)
        super(Menuscreen_window, self).__init__() 
        uic.loadUi('login.ui', self) 
        self.login_button.clicked.connect(self.menu_screen)
        self.show() 
    def login(self):             ### We can entry with our username and password
        self.username = self.username_edit.text()
        self.password = self.password_edit_2.text()
        if not os.path.isfile('user/'+self.user_name+'.json'):
            self.signup()
    def signup(self):            ### sign up methode
        self.user_info = {
            'username': self.username,
            'password': self.password,
            'level': 1,
            'time': 0
        }
        if self.password == "" and self.username =="":
            self.login_info.setText("Please enter your username & password")
        elif self.password == "":
            self.login_info.setText("Please enter your password")
        elif self.username =="":
            self.login_info.setText("Please enter your username")
        
        else:
            pass
    def menu_screen(self):
        self.cams = Main_window() 
        self.cams.show() 
        self.close() 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menuscreen_window('User')
    app.exec_()