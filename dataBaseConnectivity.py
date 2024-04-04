# # pip install myaql-connector-python
import mysql.connector
from tkinter import messagebox
# pip install email_validator
from email_validator import validate_email, EmailNotValidError
import re

# # *for using .env file
# pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()


db = mysql.connector.connect(
    host="localhost",
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database="test3" #this is the data base name that we want to connect
)

mycr=db.cursor() #this method helps in interating data in db

# #*the below line is used to create DB.
# # mycr.execute("create database test")

# mycr.execute("show databases")
# for i in mycr:
#     print(i)




def show():
    try:
        username=e1.get()
        password=e2.get()
        email=e3.get()

         # Validate username and password length
        if len(username) < 3 or len(password) < 6:
            raise ValueError("Username must be at least 3 characters and password must be at least 6 characters.") #raise is use to trigger the exception

        # Validate email using the validate_email_address library
        v = validate_email(email)
        email = v["email"]

        # Validate email using a regular expression
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")

        # Table creation statement
        create_table = """
        CREATE TABLE IF NOT EXISTS A1 (
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(50)
        )
        """
        # Insertion statement
        insert_data = "INSERT INTO A1 (username, password, email) VALUES (%s, %s, %s)"
        data_tuple = (username, password, email)

        # Execute the statement
        mycr.execute(create_table)
        mycr.execute(insert_data, data_tuple)

        # Commit changes to the database
        db.commit()
        print("inserted successfully")
    except ValueError as ve:
        # Invalid input values, show an error message
        messagebox.showerror("Input Error", str(ve))
    except EmailNotValidError as e:
        # Email is not valid, show an error message
        messagebox.showerror("Email Error", "Invalid Email")
        print(str(e))





from tkinter import*
root=Tk()
root.geometry("400x400")
root.configure(bg="orange")

l1=Label(root,text="username")
l1.place(x=20,y=50)
e1=Entry(root)
e1.place(x=90,y=50)

l2=Label(root,text="password")
l2.place(x=20,y=90)
e2=Entry(root)
e2.place(x=90,y=90)

l3=Label(root,text="email")
l3.place(x=20,y=130)
e3=Entry(root)
e3.place(x=90,y=130)



btn=Button(root,text="submit", bg="brown", fg="yellow",width=10,bd=5,command=show)
btn.place(x=69,y=170)


root.mainloop()



# !commands
# mysql -u root -p
# show databases;
# use databasename
#show tables
#select * from tableName

# *create a database
# co=db.cursor()
# co.execute("create database dbname")
# db.commit()

# *create table
# co=db.cursor()
# a="create table tableName(name varchar(10),address varchar(50),phone int(10))"
# co.execute(a)
# db.commit()

# *insert data in table
# b="insert into tablename(name,address,phone) values(%S,%s,%d)"
# value=("aman","mohali",1234567899)
# co.execute(b,value)
# db.commit()