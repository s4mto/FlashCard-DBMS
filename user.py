import psycopg2
import time
import os
import json
from datetime import datetime, timedelta
import hashlib, binascii, os


class User:
    def __init__(self,username,password):
        self.password=password
        self.username=username
        self.connect()
    def control_username(self):
        self.cur.execute("SELECT username from users where username='{}'".format(self.username))
        result=len(self.cur.fetchall())
        if result==0:
            return True
        else:
            return False
    def signup(self):
        hash_pass=self.hash_password(self.password)
        self.cur.execute("insert into users (username, password,user_level,user_time) values ('{}','{}',{},{})".format(self.username,hash_pass,1,0)) 
        self.cur.close()
        self.conn.commit()
    def login(self):
        self.cur.execute("select password from users where username='{}' and password='{}'".format(self.username,self.password))
        result=self.cur.fetchall()

        if len(result)==0:
            return False
        elif len(result)==1:
            return True
    def next_level(self):
        self.cur.execute("select user_level from users where username='{}'".format(self.username))
        level=self.cur.fetchone()[0]
        self.cur.execute("update users set user_level={} where username='{}'".format(level+1,self.username))
        self.conn.commit()
    def start_time(self):
        self.time_start=time.perf_counter()
    def stop_time(self):
        self.counter_second = time.perf_counter()-self.time_start
        self.time=round(self.counter_second)
    def progress(self):
        self.cur.execute("select user_level from users where username='{}'".format(self.username))
        level=self.cur.fetchone()[0]
        return level
    def progress_bar(self):
        return (self.progress()/250)*100
    def save_progress_time(self):
        self.stop_time()
        level=self.progress()
        self.cur.execute("select user_time from users where username='{}'".format(self.username))
        user_time=self.cur.fetchone()[0]
        user_time+=self.time
        self.cur.execute("update users set user_level={},user_time={} where username='{}'".format(level,user_time,self.username))
        self.conn.commit()
    def time_(self):
        self.cur.execute("select user_time from users where username='{}'".format(self.username))
        user_time=self.cur.fetchone()[0]
        sec=timedelta(seconds=user_time)
        d=datetime(1,1,1)+sec
        total_= str("%d hour:%d min:%d sec" % (d.hour, d.minute, d.second))
        return total_
    def connect(self):
        self.conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        self.cur = self.conn.cursor()
    def close(self):
        self.conn.close()
    def hash_password(self,p):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', p.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
    
    def verify_password(self,stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
