from PyQt5 import QtWidgets,uic
import menu
from game import Game
import psycopg2
import sys

class Statistics_window(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        self.username=username
        self.password=password 
        super(Statistics_window, self).__init__() 
        uic.loadUi('ui/statistics.ui', self)
        self.login_button_2.clicked.connect(self.back)
        self.top_precentage()
        self.show()
    def back(self): 
        self.cams = menu.menu_window(self.username)
        self.cams.show()
        self.close()


    def top_precentage(self):
        conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        cur = conn.cursor()
        cur.execute(f"""SELECT SUM(percentage),user_id FROM success_percentage ORDER BY percentage DESC WHERE user_id = {self.username} 
                    """)
        ranking = cur.fetchall()
        self.succ1.setText(                         # percentage top 5
            f'{str(ranking[0][0])}   {str(ranking[0][1])}')
        self.succ2.setText(
            f'{str(ranking[1][0])}   {str(ranking[1][1])}')
        self.succ3.setText(
            f'{str(ranking[2][0])}   {str(ranking[2][1])}')
        self.succ4.setText(
            f'{str(ranking[3][0])}   {str(ranking[3][1])}')
        self.succ5.setText(
            f'{str(ranking[4][0])}   {str(ranking[4][1])}')
        user_position = ''
        for i in ranking:
            if i[0] == self.username:
                user_position = i[0]
        self.success_level.setText(f'You are {str(user_position)} th')  # user position
        conn.commit()
        conn.close()