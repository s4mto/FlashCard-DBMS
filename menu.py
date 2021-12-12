from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QCoreApplication
import login
import game_screen
import add_level
from user import User


class menu_window(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        self.username=username
        self.password=password 
        super(menu_window, self).__init__() 
        uic.loadUi('ui/menu.ui', self) 
        self.login_()
        self.comboBox_add()
        self.progress.setProperty('value',self.user.progress_bar())
        self.logout.clicked.connect(self.login_page)
        self.quit.clicked.connect(QCoreApplication.instance().quit)
        self.play.clicked.connect(self.game_screen)
        self.add_button.clicked.connect(self.add_screen_page)
        self.show()
    def add_screen_page(self):
        self.cams = add_level.add_window() 
        self.cams.show() 
        self.close() 
    def login_page(self):
        self.cams = login.Login_window() 
        self.cams.show() 
        self.close() 
    def login_(self):
        self.user=User(self.username,self.password)
        if self.user.login():
            self.which_user.setText(self.username)
            level=str(self.user.progress())
            self.level.setText(level)
            time_=self.user.time_()
            self.total_time_show.setText(time_)
    def game_screen(self):
        self.cams = game_screen.Game_Window(self.username,self.password)
        self.cams.show() 
        self.close()
    def comboBox_add(self):
        for i in range(2,self.user.progress()+1):
            self.comboBox.addItem(str(i))
    def current_comboBox_item(self):
        self.current_combo_item=int(self.comboBox.currentText())
