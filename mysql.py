import pymysql

#connect to the database

db=pymysql.connect(host='localhost',
                        user='root',
                        password='admin',
                        database='demo2',
                        cursorclass=pymysql.cursors.DictCursor)

cursor=db.cursor()
query='INSERT INTO student VALUES("KALYAN","HP",24,"52107252HCL")'
try:

    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close