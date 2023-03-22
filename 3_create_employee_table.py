import pymysql as mq

connection_obj = mq.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "employee"
)

cursor_obj = connection_obj.cursor()
try:
   sql_command = " create table candidate_details (candidate_id INT primary key auto_increment, candidate_name varchar(50), candidate_age int(3),candidate_phone varchar(50) , candidate_email varchar(50), candidate_city varchar(20),candidate_password varchar(10))"
   
   cursor_obj.execute(sql_command)
   print(" Table created Succesfully...")
except Exception as e:
   print("Error occured....",e)