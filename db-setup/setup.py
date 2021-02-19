import mysql.connector

class db_builder:
    def __init__(self,host,user,passwd,database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database    
    def connect(self):
        db =mysql.connector.connect(
        host = self.host,      
        user = self.user,
        passwd = self.passwd,
        database = self.database
        )
        return("succesfully connected")
