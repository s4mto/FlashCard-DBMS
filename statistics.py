from PyQt5 import QtWidgets,uic
import menu
from game import Game
import psycopg2
import sys
import stat

class Statistics_window(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        self.username=username
        self.password=password 
        super(Statistics_window, self).__init__() 
        uic.loadUi('ui/statistics.ui', self)
        self.login_button_2.clicked.connect(self.back)
        self.screen()
        self.show()
        
    def back(self): 
        self.cams = menu.menu_window(self.username,self.password)
        self.cams.show()
        self.close()
    

    def screen(self):
        stat1 = stat.s(self.username,self.password)
        ranking = stat1.top_levels1()
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
        ##############################################################################################
        user_position = stat1.top_levels2()
        self.lvl_position.setText(f'You are {str(user_position)}. position!')
        ##############################################################################################
        ranking = stat1.top_precentage1()
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
        ###############################################################################################
        user_position = stat1.top_precentage2()
        self.prc_position.setText(f'You are {str(user_position)}. position!')
        ###############################################################################################
        ranking = stat1.pers_success_highest()[0]
        rowcount = stat1.pers_success_highest()[1]
        if rowcount == 0:
            pass
        if rowcount > 0:
            self.lvl_1.setText(f'{str(ranking[0][1])}')
            self.high1.setText(f'{str(ranking[0][2])} %')
        if rowcount > 1:
            self.lvl_2.setText(f'{str(ranking[1][1])}')
            self.high2.setText(f'{str(ranking[1][2])} %')
        if  rowcount >2:
            self.lvl_3.setText(f'{str(ranking[2][1])}')
            self.high3.setText(f'{str(ranking[2][2])} %')
        ################################################################################################
        ranking = stat1.pers_success_lowest()[0]
        rowcount = stat1.pers_success_lowest()[1]
        if rowcount == 0:
            pass
        if rowcount > 0:
            self.lvl_1.setText(f'{str(ranking[0][1])}')
            self.high1.setText(f'{str(ranking[0][2])} %')
        if rowcount > 1:
            self.lvl_2.setText(f'{str(ranking[1][1])}')
            self.high2.setText(f'{str(ranking[1][2])} %')
        if  rowcount >2:
            self.lvl_3.setText(f'{str(ranking[2][1])}')
            self.high3.setText(f'{str(ranking[2][2])} %')
        #################################################################################################
        self.totalnum.setText(str(stat1.total_user_count()))   # Total number of users