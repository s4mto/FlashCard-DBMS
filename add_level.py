from PyQt5 import QtWidgets,uic
import menu
from user import User

class add_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(add_window, self).__init__() 
        uic.loadUi('ui/add.ui', self)
        self.back_button.clicked.connect(self.back)
        self.show()
    def back(self):
        self.cams = menu.menu_window()
        self.cams.show()
        self.close()
    def add(self):
        pass
    def add_english(self):
        pass
    def add_dutch(self):
        pass