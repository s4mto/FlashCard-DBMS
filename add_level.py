from PyQt5 import QtWidgets,uic
import menu

class add_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(add_window, self).__init__() 
        uic.loadUi('ui/add.ui', self) 
        self.show() 