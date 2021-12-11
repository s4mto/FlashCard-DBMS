from PyQt5 import QtWidgets,uic
import login 


class credentials_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(credentials_window, self).__init__() 
        uic.loadUi('ui/credentials.ui', self) 
        self.pushButton.clicked.connect(self.login)
        self.show() 
    def login(self):
        self.cams = login.Login_window() 
        self.cams.show() 
        self.close()