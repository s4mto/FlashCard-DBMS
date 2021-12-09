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
    def menu_screen(self):
        self.cams = Main_window() 
        self.cams.show() 
        self.close() 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menuscreen_window('User')
    app.exec_()
