from database import conn, cursor





# print("-------- Expense Tracker --------")
# print("1. Add Expense.")
# print("2. View Expense.")
# print("3. Delete Expense.")
# print("4. Totoal Expanse.")
# print("5. Exit")

# choice = input("Enter your choice: ")

# while True:
#     if choice == "1":
#         pass






# else:
#     print("INVALID INPUT..")



# Registration function

def Register_function():
    name = input("Enter Your Name: ")
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")

    query = """INSERT INTO users(name,email,password)
                VALUES(%s,%s,%s)"""

    cursor.execute(query,(name, email, password))
    conn.commit()

    print("Registration Successful!..")


Register_function()

