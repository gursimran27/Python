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

cr=db.cursor() 

cr.execute("show databases")
for i in cr:
    print(i)