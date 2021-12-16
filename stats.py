import stat
import psycopg2
import os

class Stat:
    def __init__(self,username,password):
        self.password=password
        self.username=username
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        self.cur = self.conn.cursor()
    

    def top_levels1(self):
        self.cur.execute(f"""SELECT username,user_level  FROM users order by user_level desc, user_time asc
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount
    def top_levels2(self):
        self.cur.execute(f"""select * from 
(select row_number() over(),* from (select username from users order by user_level desc, user_time asc) a) b 
where username='{self.username}'""")
        user_position= self.cur.fetchall()[0][0]
        return user_position
    
    def top_percentage1(self):     # Total Success Percentage Top 5
        self.cur.execute(f"""SELECT *,ROW_NUMBER() over() FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by 2 desc) A 
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount

    def total_user_count(self):
        self.cur.execute(f"""SELECT * FROM users 
                    """)
        return self.cur.rowcount
    def top_percentage2(self):
        self.cur.execute(f"""select * from (SELECT ROW_NUMBER() over(),* FROM  
			   (select u.username,sum(sp.percentage) from users u 
				inner join success_percentage sp on u.user_id = sp.user_id 
				group by u.user_id order by sum(sp.percentage) desc,u.user_time asc) A) b where username='{self.username}'""")
        if self.cur.rowcount==0:
            user_position=0
        else:
            user_position= self.cur.fetchall()[0][0]
        return user_position

    def pers_success_highest(self):
        self.cur.execute(f"""SELECT * FROM  (select u.username,sp.current_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 desc) A WHERE username='{self.username}'
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount
    
    def pers_success_lowest(self):
        self.cur.execute(f"""SELECT * FROM  (select u.username,sp.current_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 asc) A WHERE username='{self.username}'
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount