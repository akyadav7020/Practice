import pyodbc
import pymongo

"""client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.bgcr20g.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#database = client(db)"""

"""myconn= pyodbc.connect('DRIVER={SQL Server};''SERVER=mydb708.database.windows.net;''DATABASE=my_DB1;''UID=root708;''PWD=root@123')

cursor = myconn.cursor()
cursor.execute("create table details(name varchar(20), num int)")
cursor.execute("insert into details values('Ram',609)")
data = cursor.execute("select * from details")
for i in data:
    print(i)
myconn.commit()"""