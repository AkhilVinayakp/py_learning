from os import pardir
import sqlite3

#first step creating database connection

# con = sqlite3.connect('test.db')
# # creating a cursor object for running commads
# cur = con.cursor()

# # now we can create a table using the query
# q = "create table sample (name text, id int)"
# cur.execute(q)
# con.commit()
# cur.close()
# con.close()
'''
class Db:
    def __init__(self) -> None:
        self.con:sqlite3.Connection = sqlite3.connect('test.db')
        self.cur:sqlite3.Cursor = self.con.cursor()
    
    def define_table(self):
        pass
    def insert(self,q):
        self.cur.execute(q)
        self.con.commit()
    def get_data(self, q):
        try:
            self.cur.execute(q)
            data = self.cur.fetchall()
            return data
        except sqlite3.Error as e:
            return e

'''

'''
if __name__ == "__main__":
    db = Db()
    db.insert("insert into sample {}".format(('ravi', 23)))
'''

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO SAMPLE VALUES ("Mau", 32)')
# connection.commit()


e = cursor.execute('SELECT * FROM SAMPLE')
for row in e:
    print(row)
cursor.execute('SELECT * FROM SAMPLE WHERE NAME = "Mau"')
t = cursor.fetchall()
print(t)