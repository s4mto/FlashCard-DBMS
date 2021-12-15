import psycopg2

class Game:
    def __init__(self,level,language='english'):
        self.level=level
        self.language=language
        self.known_words = 0
        self.total_words = 0
        self.begin()
    def begin(self):
        self.connect()
        self.cur.execute("select dutch,english from words where word_level='{}'".format(self.level))
        self.level_words=self.cur.fetchall()
    def flashcard(self):
        return self.level_words[0]
    def progress(self, choice):
        if choice:
            self.true_button_()
        else: 
            self.false_button_()
        return [self.known_words,self.total_words]  
    def true_button_(self):
        self.known_words+=1
        self.total_words+=1
        self.level_words.pop(0)
    def false_button_(self):
        self.total_words+=1
        self.level_words.append(self.level_words[0])
        self.level_words.pop(0)
    def success_percentage(self):
        if self.known_words==0:
            return 0
        else:
            return (self.known_words/self.total_words)*100

    def connect(self):
        self.conn = psycopg2.connect(database = "flashcard",user = "postgres",host = "localhost",password = "1903")
        self.cur = self.conn.cursor()
    def close(self):
        self.conn.close()

