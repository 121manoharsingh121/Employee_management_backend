import pymysql as mq
import os
# import 1_create_employee_database 
# import 2_admin_login_details 
# import 3_create_employee_table 

connection_obj = mq.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "employee"
)

    
   
def login_authorization(sdata,u_name):       #function to check authorisation of user
    count=0
    if sdata==None:
        print("No User Exits")
    else:
        u_password= input("Enter  Password  : ")
        user=sdata[0]
        password=sdata[1]
        # print("user: ",user)
        # print("password: ",password)
        
        if  password==u_password:
             print("Welcome  "+user)
             count+=1
        else:
             print("wrong password")
    return count

def registration_form():                     # function for Insert data (Registration Form)
    os.system('cls')
    print(" NEW REGISTRATION FORM")
    c_name=input("Enter your Name: ")
    c_age=int(input("Enter your Age: "))
    c_phone=(input("Enter your Mobile Number: "))
    c_email=input("Enter your Email: ")
    c_city=input("Enter your city: ")
    c_password=input("Enter Your Password: ")
    
    cursor_obj = connection_obj.cursor()
    try:
        insert_command = "insert into candidate_details(candidate_name , candidate_age, candidate_phone,candidate_email , candidate_city, candidate_password) values(%s,%s,%s,%s,%s,%s)"
        data=(c_name, c_age,c_phone,c_email, c_city,c_password)
        cursor_obj.execute(insert_command,data)
        connection_obj.commit()
        print("\n")
        print("Form Submitted Successfuly....")
        print("\n")
    except Exception as e:
        print("Error occured",e)

def update(candidate_id):                    # function defination for update record
    
    c_id=candidate_id
    cursor_obj = connection_obj.cursor()
    c_name=input("Enter your Name: ")
    c_age=int(input("Enter your Age: "))
    c_phone=(input("Enter your Mobile Number: "))
    c_email=input("Enter your Email: ")
    c_city=input("Enter your city: ")
    c_password=input("Enter Your Password: ")
    
    try:
        sql_command = "update candidate_details set candidate_name=%s , candidate_age=%s , candidate_phone=%s,candidate_email=%s , candidate_city =%s ,candidate_password=%s where candidate_id=%s"

        data=(c_name,c_age,c_phone,c_email,c_city,c_password,c_id)
        cursor_obj.execute(sql_command,data)
        connection_obj.commit()
        print("\n")
        print("Form Updated Successfully....")
        print("\n")
        display_candidate_form(c_name)
    
    except Exception as e:
       print(" Some error Occured...",e)

def delete_form(candidate_id):               # function for delete record 
    id=candidate_id
    cursor_obj = connection_obj.cursor()
    sql_command = "delete from candidate_details where candidate_id=%s"
     
    try:
       cursor_obj.execute(sql_command,id)
       connection_obj.commit()
       print("\n")
       print("Record Deleted Successfully")
       print("\n")

    except Exception as e:
       print(" Some error Occured...",e)
      

def display_all_record():                    # Function  for display record of a all record
    cursor_obj = connection_obj.cursor()
    try:
       sql_command="select candidate_id,candidate_name,candidate_age, candidate_phone,candidate_email,candidate_city from candidate_details "
       cursor_obj.execute(sql_command)
       sdata=cursor_obj.fetchall()
    except Exception as e:
       print("Some Error occured...")

    if sdata==None:
        print("\n")
        print("No record available.....")
        print("\n")
    else:
        print("{:<20} {:<15} {:<20} {:<20} {:<20} {:<10}".format("candidate Id","Candidate Name "," Age","phone"," Email","City"))
        for s in sdata:
          print("{:<20} {:<15} {:<20} {:<20} {:<20} {:<10}".format(s[0],s[1],s[2],s[3],s[4],s[5]))

def display_candidate_form(candidate_name):  # Function for display record of a single record
    cursor_obj = connection_obj.cursor()
    name=candidate_name
    try:
       sql_command="select candidate_id,candidate_name,candidate_age, candidate_phone,candidate_email,candidate_city ,candidate_password from candidate_details where candidate_name = '"+name+"'"
       cursor_obj.execute(sql_command)
       sdata=cursor_obj.fetchone()
       if sdata==None:
          print("\n")
          print("No record available.......")
          print("\n")
       else:
          print("{:<20} {:<15} {:<20} {:<20} {:<20} {:<10} {:<10}".format("Candidate Id","Candidate Name "," Age","phone"," Email","City","Password"))
          print("{:<20} {:<15} {:<20} {:<20} {:<20} {:<10} {:<10}".format(sdata[0],sdata[1],sdata[2],sdata[3],sdata[4],sdata[5],sdata[6]))
          c_id=sdata[0]
        
       return c_id
    except Exception as e:
       print("Some Error occured...")
   
def search_record(candidate_id):             # Function to search record
      cursor_obj = connection_obj.cursor()
      id=candidate_id
      try:
       sql_command="select candidate_id,candidate_name,candidate_age, candidate_phone,candidate_email,candidate_city ,candidate_password from candidate_details where candidate_id = '"+id+"'"
       cursor_obj.execute(sql_command)
       sdata=cursor_obj.fetchone()
       data=0
       if sdata==None:
          data+=1
       return data
      except Exception as e:
       print("Some Error occured...")
        



def candidate_login():                       # main()---> called  Candidate_page() ---->called candidate_login()
    os.system('cls')
    print("\n")
    print("         CANDIDATE LOG IN      ")
    print("\n")
    cursor_obj = connection_obj.cursor()
    c_name= input("Enter candidate Name : ")
    try:
       sql_command="select candidate_name,candidate_password from candidate_details where candidate_name = '"+c_name+"'"
       cursor_obj.execute(sql_command)
       sdata=cursor_obj.fetchone()
    except Exception as e:
       print("Some Error occured...",e)
       
    count=login_authorization(sdata,c_name)
    if count==1:
        os.system('cls') 
        c_id=display_candidate_form(c_name)
        while True:
          print('''
1         Update Record 
2         Delete Record
3         Return to Previous Menu
4         Return To Main Menu
5         Exit

         ''')

          c_choice=input("Enter your choice: ")
          match c_choice:
            case '1':
             update(c_id)
            case '2':
              print('''
              Are you sure you want to delete your record..?
              Enter 1 for yes
              Enter 2 for No 
                    ''')
              choice=input("Enter your choice: ")
              if choice=='1':
                 delete_form(c_id)
                 candidate_page()
              else:
                 continue
            case '3':
             candidate_page()
            case '4':
             main()
            case '5':
             exit()
            case _:
             print("Wrong Input")
            
           
    else:
          print("Wrong Authorization")
          candidate_page()
           

def admin_login():                           # main()----> called  admin_login()
    os.system('cls') 
    print("           ADMIN LOGIN  PAGE       ") 
    print("\n")   
    cursor_obj = connection_obj.cursor()
    u_name= input("Enter Admin Name : ")
    try:
       sql_command="select user_name,user_password from login_table where user_name = '"+u_name+"'"
       cursor_obj.execute(sql_command)
       sdata=cursor_obj.fetchone()
    except Exception as e:
       print("Some Error occured...")
    
    count=login_authorization(sdata,u_name)
    if count==1:
       while True:
         print('''
1  Display all records
2  Delete record
3  Return To Main Menu
4  Exit
       ''')
    
         a_choice=input("Enter your choice: ")
         match a_choice:
            case '1':
             display_all_record()
            case '2':
             c_id=input("Enter candidate id to delete: ")
             data=search_record(c_id)
             if data==1:
                print("\n")
                print("Enter valid id")
                print("\n")
                display_all_record()
                continue
             else:
                delete_form(c_id)
            case '3':
             main()
            case '4':
             exit()
            case _:
             print("Wrong Input")
    else:
          print("Wrong Authorization")



def candidate_page():                        #function defination for candidate login
    
    print("         WELCOME TO CANDIDATE PAGE        ")
    print("\n")
    print('''
    1    New Registration
    2    Already Registred
    3    Return To Main Menu
    4    Exit
    ''')

    choice=input("Enter Your Choice:")
    match choice:
       case '1':
        registration_form()
       case '2':
         candidate_login()
       case '3':
          main()
       case '4':
          exit()
       case _:
          print("Wrong input")
          candidate_page()


def main():                                  #main function
  os.system('cls')
  print(" Welcom:")
  while True:
   print('''

1     Admin login
2     Candidate login
3     Exit

''')
   c_choice=input("Enter your Choice : ")
   match c_choice:
        case '1':
         admin_login()
        case '2':
         candidate_page()
        case '3':
         exit()
        case _:
         print("Wrong Input")

if __name__ == "__main__":
    main()

