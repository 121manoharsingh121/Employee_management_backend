import pymysql as mq
connection_obj = mq.Connect(
    host = "localhost",
    user = "root",
    password = "root"
)
print(connection_obj)

cursor_obj = connection_obj.cursor()
try:
    db = "create database employee"
    cursor_obj.execute(db)
    print("Database Created successfully...")

except :
    print("Some error occured.....")

