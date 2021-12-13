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
        self.top_levels()
        self.top_precentage()
        self.pers_success_highest()
        self.pers_success_lowest()
        self.show()
    def back(self): 
        self.cams = menu.menu_window(self.username)
        self.cams.show()
        self.close()
    def top_levels(self):
        conn = psycopg2.connect(database = "Flashcards",user = "postgres",host = "localhost",password = "Metehan")
        cur = conn.cursor()
        cur.execute(f"""SELECT username, user_level, ORDER BY user_level DESC FROM users
                    """)
        ranking = cur.fetchall()
        
        self.totalnum.setText(str(cur.rowcount))     # Total number of users
        
        self.level1.setText(                         # level top 5
            f'{str(ranking[0][2])} . {str(ranking[0][0])}   ({str(ranking[0][1])})')
        self.level2.setText(
            f'{str(ranking[1][2])} . {str(ranking[1][0])}   ({str(ranking[1][1])})')
        self.level3.setText(
            f'{str(ranking[2][2])} . {str(ranking[2][0])}   ({str(ranking[2][1])})')
        self.level4.setText(
            f'{str(ranking[3][2])} . {str(ranking[3][0])}   ({str(ranking[3][1])})')
        self.level5.setText(
            f'{str(ranking[4][2])} . {str(ranking[4][0])}   ({str(ranking[4][1])})')
        user_position = ''
        for i in ranking:
            if i[0] == self.username:
                user_position = i[2]
        self.rank_level.setText(f'You are {str(user_position)} th')  # user position
        conn.commit()
        conn.close()

    def top_precentage(self):
        conn = psycopg2.connect(database = "Flashcards",user = "postgres",host = "localhost",password = "Metehan")
        cur = conn.cursor()
        cur.execute(f"""SELECT user_id, 20 * 100.0 / total_words ORDER BY (20 * 100.0 / total_words) DESC FROM statistics
                    """)
        ranking = cur.fetchall()
        self.succ1.setText(                         # percentage top 5
            f'{str(ranking[0][2])} . {str(ranking[0][0])}   ({str(ranking[0][1])})')
        self.succ2.setText(
            f'{str(ranking[1][2])} . {str(ranking[1][0])}   ({str(ranking[1][1])})')
        self.succ3.setText(
            f'{str(ranking[2][2])} . {str(ranking[2][0])}   ({str(ranking[2][1])})')
        self.succ4.setText(
            f'{str(ranking[3][2])} . {str(ranking[3][0])}   ({str(ranking[3][1])})')
        self.succ5.setText(
            f'{str(ranking[4][2])} . {str(ranking[4][0])}   ({str(ranking[4][1])})')
        user_position = ''
        for i in ranking:
            if i[0] == self.username:
                user_position = i[2]
        self.success_level.setText(f'You are {str(user_position)} th')  # user position
        conn.commit()
        conn.close()

    def pers_success_highest(self):
        conn = psycopg2.connect(database = "Flashcards",user = "postgres",host = "localhost",password = "Metehan")
        cur = conn.cursor()
        cur.execute(f"""SELECT user_id, 20 * 100.0 / total_words ORDER BY (20 * 100.0 / total_words) DESC FROM statistics LIMIT 3 WHERE username = {self.username} 
                    """)
        ranking = cur.fetchall()
        self.succ1.setText(                         # Personal Success Percentage Highest 3 
            f'{str(ranking[0][2])} . {str(ranking[0][0])}   ({str(ranking[0][1])})')
        self.succ2.setText(
            f'{str(ranking[1][2])} . {str(ranking[1][0])}   ({str(ranking[1][1])})')
        self.succ3.setText(
            f'{str(ranking[2][2])} . {str(ranking[2][0])}   ({str(ranking[2][1])})')

    def pers_success_lowest(self):
        conn = psycopg2.connect(database = "Flashcards",user = "postgres",host = "localhost",password = "Metehan")
        cur = conn.cursor()
        cur.execute(f"""SELECT user_id, 20 * 100.0 / total_words ORDER BY (20 * 100.0 / total_words) ASC FROM statistics LIMIT 3 WHERE username = {self.username} 
                    """)
        ranking = cur.fetchall()
        self.succ1.setText(                         # Personal Success Percentage Lowest 3 
            f'{str(ranking[0][2])} . {str(ranking[0][0])}   ({str(ranking[0][1])})')
        self.succ2.setText(
            f'{str(ranking[1][2])} . {str(ranking[1][0])}   ({str(ranking[1][1])})')
        self.succ3.setText(
            f'{str(ranking[2][2])} . {str(ranking[2][0])}   ({str(ranking[2][1])})')