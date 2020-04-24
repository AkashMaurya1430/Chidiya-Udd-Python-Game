import sqlite3

conn = sqlite3.connect("chidiya.db")
c = conn.cursor()
'''
c.execute("CREATE TABLE IF NOT EXISTS animals(No INT, Name TEXT, Value INT)")

c.execute("INSERT INTO animals VALUES(0,'Lion',0)")
c.execute("INSERT INTO animals VALUES(1,'Crow',1)")
c.execute("INSERT INTO animals VALUES(2,'Tiger',0)")
c.execute("INSERT INTO animals VALUES(3,'Sparrow',1)")
c.execute("INSERT INTO animals VALUES(4,'Duck',1)")
c.execute("INSERT INTO animals VALUES(5,'Deer',0)")
c.execute("INSERT INTO animals VALUES(6,'Elephant',0)")
c.execute("INSERT INTO animals VALUES(7,'Eagle',1)")
c.execute("INSERT INTO animals VALUES(8,'Kite',1)")
c.execute("INSERT INTO animals VALUES(9,'Aeroplane',1)")
'''
conn.commit()
names = ()
values = ()

r=c.execute("Select Name,Value from animals order by RANDOM()")
for n,v in r.fetchall():
    names =names+(n,)
    values = values+(v,)
conn.close()
print(names)
print(values)
