from PyQt5 import QtWidgets,uic


class main_window(QtWidgets.QMainWindow):
    def __init__(self): 
        super(main_window, self).__init__() 
        uic.loadUi('menu.ui', self) 
        self.show() 
