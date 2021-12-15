from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QCoreApplication
import login
import game_screen
from user import User
import add_ui


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
        # self.add_button.clicked.connect(self.add_screen_page)
        self.add_button.clicked.connect(self.add_page)
        self.comboBox.setCurrentIndex(self.user.progress()-1)
        self.show()
    # def add_screen_page(self):
    #     self.cams = add_level.add_window() 
    #     self.cams.show() 
    #     self.close() 
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
            self.total_time_show.setText(self.user.time_())
    def game_screen(self):
        self.current_comboBox_item()
        self.cams = game_screen.Game_Window(self.username,self.password,self.current_combo_item)
        self.cams.show() 
        self.close()
    def comboBox_add(self):
        for i in range(2,self.user.progress()+1):
            self.comboBox.addItem(str(i))
    def current_comboBox_item(self):
        self.current_combo_item=int(self.comboBox.currentText())
    def add_page(self):
        self.cams = add_ui.add_Window(self.username,self.password) 
        self.cams.show() 
        self.close() 
