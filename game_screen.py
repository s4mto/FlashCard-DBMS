from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QCoreApplication,QTimer
import game
import menu
from user import User

class Game_Window(QtWidgets.QMainWindow):
    def __init__(self,username,password,combo_level,timer):
        self.timer=int(timer)
        self.combobox_level=combo_level
        self.username=username
        self.password=password
        super(Game_Window, self).__init__() 
        uic.loadUi('ui/gamescreen.ui', self)
        self.login_()
        self.pushButton.clicked.connect(self.save_time_buttons)
        self.pushButton.clicked.connect(self.save_level_buttons)
        self.pushButton.clicked.connect(self.menu_back)
        self.progressBar.setProperty('value',0)
        self.time_lcd_word.display(11)
        self.show()
        self.next_level.setVisible(False)
        self.next_level.clicked.connect(self.save_level_buttons)
        self.next_level.clicked.connect(self.level_up)
        self.start=True #to start counter
        self.count=self.timer*10
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
    def showTime(self):
        if self.start:
            self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 255, 0);") 
            if self.game.known_words<self.game.words_count():
                self.word.setText(self.game.flashcard()[0]) #to show dutch words
                self.count -= 1
                if self.count == -1:
                    self.start = False
                    self.true_button.clicked.connect(self.true_button_)
                    self.false_button.clicked.connect(self.false_button_)
                    self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 0,255);")  
                    self.word.setText(self.game.flashcard()[1]) #to show meaning of dutch words after 3 seconds
            else:
                self.word.setText("Gefeliciteerd") # after finishing level to show gefeliciteerd
                self.next_level.setVisible(True) #next level button activated
        if self.start:
            time_seconds = int(self.count/10)
            self.time_lcd_word.display(time_seconds)
    def menu_back(self):
        self.cams = menu.menu_window(self.username,self.password)
        self.cams.show() 
        self.close()
    def login_(self):
        self.user=User(self.username,self.password)
        if self.user.login():
            self.start_()
            self.user.start_time()
    def start_(self):
        self.level.setText(self.combobox_level)
        self.game=game.Game(self.combobox_level)
    def level_up(self):
        self.user.next_level(self.game.success_percentage(),self.game.level)
        self.level.setText(str(self.combobox_level))
        self.game=game.Game(self.combobox_level)
    def true_button_(self):
        if self.start == False:
            self.game.progress(True)
            self.twentyplus.display(int(self.game.known_words))
            self.known_word_lcd.display(int(self.game.total_words))
            self.progressBar.setProperty('value',self.game.success_percentage())
            self.time_improve()
    def false_button_(self):
        if self.start == False:
            self.game.progress(False)
            self.twentyplus.display(int(self.game.known_words))
            self.known_word_lcd.display(int(self.game.total_words))
            self.progressBar.setProperty('value',self.game.success_percentage())
            self.time_improve()
    def time_improve(self):
        self.start=True
        self.count=(self.timer)*10
    def save_level_buttons(self):
        self.next_level.setVisible(False)
        if self.game.known_words==self.game.words_count():
            self.user.next_level(self.game.success_percentage(),self.combobox_level)
    def save_time_buttons(self):
        self.user.save_progress_time()
