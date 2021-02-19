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
        return db
    def mk_table(self, table_name,variable_query):
        mydb = db_builder.connect(self)
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE "+table_name+"("+variable_query+")")
        return "succesfuly made table"
p1 = db_builder("localhost","root","new_password","test")
print(p1.connect())
print(p1.mk_table("User","Name VARCHAR(255), Password VARCHAR(255)"))