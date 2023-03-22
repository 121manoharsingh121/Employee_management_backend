import pymysql as mq

connection_obj = mq.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "employee"
)

cursor_obj = connection_obj.cursor()

try:

        u_name=input("Enter your Name: ") #admin
        u_password=input("Enter your password: ") #admin@123
        

        insert_command = "insert into login_table(user_name , user_password) values(%s,%s)"

        data=(u_name, u_password)
        cursor_obj.execute(insert_command,data)
        connection_obj.commit()
        print(" Data inserted successfuly....")
except Exception as e:
        print("Error occured",e)


