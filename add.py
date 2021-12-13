from PyQt5 import QtWidgets,uic
from menu import menu_window


class add_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(add_Window, self).__init__() 
        uic.loadUi('ui/add.ui', self)
        self.back.clicked.connect(self.menu_page)
        self.show() 

    def menu_page(self):
        self.cams = menu_window() 
        self.cams.show() 
        self.close() 
    
    def add_level(self):
        level_name = self.levelname_edit.text()
        dutch_word = self.dutchword_edit.text()
        english_word = self.english_edit.text()
        if level_name == None or dutch_word == None or english_word == None:
            QtWidgets.QMessageBox.about(self,'Please enter all the necessary information!')
        else:
            pass