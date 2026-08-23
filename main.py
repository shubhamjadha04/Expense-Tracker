from database import conn, cursor


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
    track_expense()


# Login function
def login_function():
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
        track_expense()

    else:
        print("Invalid email or password..")
    

# The main expense tarctor function

def track_expense():
    print("-------- Expense Tracker --------")
    print("1. Add Expense.")
    print("2. View Expense.")
    print("3. Delete Expense.")
    print("4. Totoal Expanse.")
    print("5. Exit")

    choice = input("Enter your choice: ")

    while True:
        if choice == "1":
            pass





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
    Register_function()

elif log_choice == "2":
    login_function()
else:
    print("Invalid Option..")


