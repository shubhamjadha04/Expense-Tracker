import mysql.connector

connect = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "shubham2004",
    database = "Expenses"
    )

cursor = connect.cursor()

print("connection has done.")