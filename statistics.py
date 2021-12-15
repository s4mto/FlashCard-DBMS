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
        self.cams = menu.menu_window(self.username,self.password)
        self.cams.show()
        self.close()
    def top_levels(self):  # Level Top 5
        conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        cur = conn.cursor()
        cur.execute(f"""SELECT username, user_level  FROM users ORDER BY 2 DESC, 1 
                    """)
        ranking = cur.fetchall()
        self.level1.setText(f'{str(ranking[0][0])}')
        self.lvl1.setText(f'{str(ranking[0][1])}')
        self.level2.setText(f'{str(ranking[1][0])}')
        self.lvl2.setText(f'{str(ranking[1][1])}')
        self.level3.setText(f'{str(ranking[2][0])}')
        self.lvl3.setText(f'{str(ranking[2][1])}')
        self.level4.setText(f'{str(ranking[3][0])}')
        self.lvl4.setText(f'{str(ranking[3][1])}')
        self.level5.setText(f'{str(ranking[4][0])}')
        self.lvl5.setText(f'{str(ranking[4][1])}')

        #SELECT ROW_NUMBER() OVER(),A.username, A.user_level, A.user_time FROM (select * from users order by user_level desc, user_time asc) A where username= 'ayşe'
        cur.execute(f"""SELECT ROW_NUMBER() OVER(),A.username, A.user_level, A.user_time FROM (select * from users order by user_level desc, user_time asc) A where username= '{self.username}'
                    """)
        user_position= cur.fetchall()[0][0]
        self.lvl_position.setText(f'You are {str(user_position)}. position!')  # user position
        conn.commit()
        conn.close()

    def top_precentage(self):     # Total Success Percentage Top 5
        conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        cur = conn.cursor()
        cur.execute(f"""SELECT *,ROW_NUMBER() over() FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by 2 desc) A 
                    """)
        ranking = cur.fetchall()

        self.totalnum.setText(str(cur.rowcount))     # Total number of users

        self.succ1.setText(f'{str(ranking[0][0])}')
        self.succ2.setText(f'{str(ranking[1][0])}')
        self.succ3.setText(f'{str(ranking[2][0])}')
        self.succ4.setText(f'{str(ranking[3][0])}')
        self.succ5.setText(f'{str(ranking[4][0])}')
        self.succ1_1.setText(f'{str(ranking[0][1])}')
        self.succ2_1.setText(f'{str(ranking[1][1])}')
        self.succ3_1.setText(f'{str(ranking[2][1])}')
        self.succ4_1.setText(f'{str(ranking[3][1])}')
        self.succ5_1.setText(f'{str(ranking[4][1])}')
        
        #SELECT ROW_NUMBER() over(),* FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by sum(sp.percentage) desc,u.user_time asc) A 
#where username='mercan'

        cur.execute(f"""SELECT ROW_NUMBER() over(),* FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by sum(sp.percentage) desc,u.user_time asc) A 
where username='{self.username}'
                    """)
        user_position= cur.fetchall()[0][0]
        self.prc_position.setText(f'You are {str(user_position)}. position!')  # user position
        conn.commit()
        conn.close()
        

    def pers_success_highest(self):  # Personal Success Percentage Highest 3
        conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM  (select u.username,sp.currente_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 desc) A WHERE username='{self.username}'
                    """)
        ranking = cur.fetchall()
        if cur.rowcount == 0:
            pass
        if cur.rowcount > 0:
            self.lvl_1.setText(f'{str(ranking[0][1])}')
            self.high1.setText(f'{str(ranking[0][2])} %')
        if cur.rowcount > 1:
            self.lvl_2.setText(f'{str(ranking[1][1])}')
            self.high2.setText(f'{str(ranking[1][2])} %')
        if  cur.rowcount >2:
            self.lvl_3.setText(f'{str(ranking[2][1])}')
            self.high3.setText(f'{str(ranking[2][2])} %')
        conn.commit()
        conn.close()

    def pers_success_lowest(self):       # Personal Success Percentage Lowest 3
        conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM  (select u.username,sp.currente_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 asc) A WHERE username='{self.username}'
                    """)
        ranking = cur.fetchall()
        if cur.rowcount == 0:
            pass
        if cur.rowcount > 0:
            self.lvl_4.setText(f'{str(ranking[0][1])}')
            self.low1.setText(f'{str(ranking[0][2])} %')
        if cur.rowcount > 1:
            self.lvl_5.setText(f'{str(ranking[1][1])}')
            self.low2.setText(f'{str(ranking[1][2])} %')
        if  cur.rowcount > 2:
            self.lvl_6.setText(f'{str(ranking[2][1])}')
            self.low3.setText(f'{str(ranking[2][2])} %')