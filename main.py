from database import conn, cursor


# Registration function
def register_user():
    name = input("Enter Your Name: ")
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")

    query = """INSERT INTO users(name,email,password)
                VALUES(%s,%s,%s)"""

    cursor.execute(query,(name, email, password))
    conn.commit()

    print("Registration Successful!..")
    expense_menu()


# Login function
def login_user():
    email = input("Enter Your email: ")
    password = input("Enter Your password: ")

    query= """
            SELECT * FROM users 
            WHERE email = %s AND password = %s
    """
    cursor.execute(query,(email,password))
    user = cursor.fetchone()

    if user:
        print("Login Successful!..")
        expense_menu()

    else:
        print("Invalid email or password..")
    




# The main expense tarctor menu
def expense_menu():
    print("-------- Expense Tracker --------")
    print("1. Add Expense.")
    print("2. View Expense.")
    print("3. Delete Expense.")
    print("4. Totoal Expanse.")
    print("5. Exit")

    choice = input("Enter your choice: ")

    while True:
        if choice == "1":
            Category = input("Enter the categery: ")
            amount  = int(input("Enter the amount: "))
            Description = input("Enter the Description: ")

            query = """
                        INSERT INTO 
                        
                            """





        elif choice == "5":
            print("Exited...")
            break
        else:
            print("INVALID INPUT..")
            break
        




print("----Register--or--login----")
print("1. Register: ")
print("2. login: ")

log_choice = input("Enter your choice: ")
if log_choice == "1":
    register_user()
elif log_choice == "2":
    login_user()
else:
    print("Invalid Option..")


