import psycopg2 
class User:
        def __init__(self,username,password):
                self.username = username
                self.password = password
                self.connect()


        def control_username(self):
            self.cur.execute("SELECT username from users where username='{}'".format(self.username))
            result=len(self.cur.fetchall())
            if result==0:
                return True
            else:
                return False

        def connect(self):
                self.con =psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "password")
                self.cur = self.con.cursor()
        
        def signup(self):
                self.cur.execute("insert into users(username,password,user_level,user_time)values('{}','{}',{},{})".format(self.username,self.password,1,0))
                self.cur.close()
                self.conn.commit()