from PyQt5 import QtWidgets,uic
import menu
from user import User

class add_Window(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        self.username =username
        self.password = password
        super(add_Window, self).__init__() 
        uic.loadUi('ui/add.ui', self)
        self.back.clicked.connect(self.back_menu)
        self.add.clicked.connect(self.add_level)
        self.show() 
    def back_menu(self):
        self.cams = menu.menu_window(self.username,self.password) 
        self.cams.show() 
        self.close() 
    def add_level(self):
        level_name = self.levelname_edit.text()
        dutch_word = self.dutchword_edit.text()
        english_word = self.english_edit.text()
        User1 = User(self.username,self.password)
        User1.login()
        User1.add_level(level_name,dutch_word,english_word)
        self.dutchword_edit.clear()
        self.english_edit.clear()
        
