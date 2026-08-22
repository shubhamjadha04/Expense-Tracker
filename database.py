import mysql.connector

conn = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "shubham2004",
    database = "Expenses"
    )

cursor = conn.cursor()
