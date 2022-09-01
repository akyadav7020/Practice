import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="root@123")
cursor = mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())  # all databases
"""database = "testing"
cursor.execute("create database if not exists {}".format(database))"""
#cursor.execute("drop database testing")

cursor.execute("use testing")

"""table = "table2"
cursor.execute("create table if not exists {}(name varchar(20),num int)".format(table))"""

#cursor.execute("insert into table2 values('abhay',756)")
#mydb.commit()

check='name'
cursor.execute("select {} from table2".format(check))
names=(cursor.fetchall())
names_list =set()
for i in range(len(names)):
    names_list.add(names[i][0])

table = 'table2'
data = [{'abhay':708},{'rahu':708}, {"ram": 68},{'syam':878},{'gya':98},{'hsh':99}]
for i in range(len(data)):
    for key in data[i]:
        j=key
    if j not in names_list:
        cursor.execute("insert into {} values('{}','{}')".format(table,j,data[i][j]))
        mydb.commit()


cursor.execute("select * from table2")

print(cursor.fetchall())