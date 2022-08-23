from flask import Flask,request,jsonify
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",passwd="root@123")
cursor = mydb.cursor()

app = Flask(__name__)

@app.route('/test',methods=['POST','GET'])
def test():
    if request.method =='GET':
        name = request.args.get('name')
        num = request.args.get('num')
        cursor.execute("create database if not exists abhay")
        cursor.execute("use abhay")
        cursor.execute("create table if not exists test (name varchar(20),num int)")
        cursor.execute("insert into test values(%s, %s)",(name,num))
        mydb.commit()
        cursor.execute("select * from test")
        res = cursor.fetchall()
        return res
    if request.method =='POST':
        name = request.json['name']
        num = request.json['num']
        cursor.execute("create database if not exists abhay")
        cursor.execute("use abhay")
        cursor.execute("create table if not exists test (name varchar(20),num int)")
        cursor.execute("insert into test values(%s, %s)",(name,num))
        mydb.commit()
        cursor.execute("select * from test")
        res = cursor.fetchall()
        return jsonify(res)

if __name__ == '__main__':
    app.run()