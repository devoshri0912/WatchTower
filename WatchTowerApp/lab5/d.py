import sqlite3
conn=sqlite3.connect('test.db')
print("opened sucessfully")
c=conn.cursor()
conn.execute("DROP TABLE COMPANY")
c.execute("CREATE TABLE COMPANY (ID INT PRIMARY KEY,NAME VARCHAR(20),AGE INT,ADDRESS VARCHAR(20),SALARY FLOAT)")
print("table created")
many=[(1,'tesla',34,'america',100000),(2,'colgate',35,'india',50000)]
c.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?)",many)

com=c.execute("SELECT * FROM COMPANY")
for row in com:
    print ("ID= ",row[0])
    print ("NAME= ",row[1])
    print ("AGE= ",row[2])
    print ("ADDRESS= ",row[3])
    print ("SALARY= ",row[4])


c.execute("SELECT * FROM COMPANY")
#print(c.fetcha())
#print(c.fetchall()[0][1])

items=c.fetchall()

print(items[1])

for item in items:
    print(item)
    print(item[0])
    print(item[1])
    print(item[2])


itemss=c.execute("SELECT rowid, * from company ")

for item in itemss:
    print(item)

c.execute("select * from company where name='tesla'")
i=c.fetchall()

for f in i:
    print(f)

conn.close()