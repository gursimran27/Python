import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()



db = mysql.connector.connect(
    host="localhost",
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    # database="test" #this is the data base name that we want to connect
)


mycr=db.cursor() #this method helps in interating with db

# #*the below line is used to create DB.
mycr.execute("create database test3")

# #the below line show all DB names
# mycr.execute("show databases")
# for i in mycr:
#     print(i)