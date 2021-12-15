import psycopg2

class s:
    def __init__(self,username,password):
        self.password=password
        self.username=username
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        self.cur = self.conn.cursor()
    

    def top_levels1(self):
        self.cur.execute(f"""SELECT username, user_level  FROM users ORDER BY 2 DESC, 1 
                    """)
        self.ranking = self.cur.fetchall()
        return self.ranking
    def top_levels2(self):
        self.cur.execute(f"""SELECT ROW_NUMBER() OVER(),A.username, A.user_level, A.user_time FROM (select * from users order by user_level desc, user_time asc) A where username= '{self.username}'
                    """)
        user_position= self.cur.fetchall()[0][0]
        return user_position
    
    def top_precentage1(self):     # Total Success Percentage Top 5
        self.cur.execute(f"""SELECT *,ROW_NUMBER() over() FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by 2 desc) A 
                    """)
        ranking = self.cur.fetchall()
        return ranking

    def total_user_count(self):
        self.cur.execute(f"""SELECT * FROM users 
                    """)
        return self.cur.rowcount
    def top_precentage2(self):
        self.cur.execute(f"""SELECT ROW_NUMBER() over(),* FROM  (select u.username,sum(sp.percentage) from users u inner join success_percentage sp on u.user_id = sp.user_id group by u.user_id order by sum(sp.percentage) desc,u.user_time asc) A 
                        where username='{self.username}'
                    """)
        user_position= self.cur.fetchall()[0][0]
        return user_position

    def pers_success_highest(self):
        self.cur.execute(f"""SELECT * FROM  (select u.username,sp.currente_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 desc) A WHERE username='{self.username}'
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount
    
    def pers_success_lowest(self):
        self.cur.execute(f"""SELECT * FROM  (select u.username,sp.currente_level,sp.percentage from users u inner join success_percentage sp on u.user_id = sp.user_id  order by 3 asc) A WHERE username='{self.username}'
                    """)
        ranking = self.cur.fetchall()
        return ranking,self.cur.rowcount
