from database import conn, cursor
import mysql


# Registration function
def register_user():
    name = input("Enter Your Name: ")
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")

    query = """INSERT INTO users(name,email,password)
                VALUES(%s,%s,%s)"""

    cursor.execute(query,(name, email, password))
    conn.commit()

    user_id =   cursor.lastrowid
    print("Registration Successful!..")
    print(f"Your User Id = :{user_id}")
    login_user()
    



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
        user_id = user[0]
        expense_menu(user_id)

    else:
        print("Invalid email or password..")


# the add expense function
def add_expense(user_id):
    try:
        category = input("Enter the categery: ")
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: ")

        query = """ 
                INSERT INTO expenses 
                (user_id,category, amount, description,expense_date)
                VALUES(%s,%s,%s,%s,NOW())
                """
        cursor.execute(query,(user_id,category,amount,description))
        conn.commit()
        print(f"The amount added to {category} category..")

    except ValueError:
        print("Amount must be a valid number..")

    except mysql.connection.Error as err:
        print("Database error: ",err)

    except Exception as e:
        print("Unexpected error:",e)

# view expense function
def view_expense(user_id):
    query = """
            SELECT category, amount, description, expense_date FROM expenses 
            WHERE user_id = %s"""

    cursor.execute(query,(user_id,))
    expenses = cursor.fetchall()

    if expenses:
        for expense in expenses:
                print(f"""
            Category    : {expense[0]}
            Amount      : ₹{expense[1]}
            Description : {expense[2]}
            Date        : {expense[3]}
            -----------------------------
            """)
    else:
        print("No expenses found !..")


# Delete expense function
def delete_expnse(user_id):
        
        query = """
        SELECT expense_id, category, amount, description, expense_date
        FROM expenses
        WHERE user_id = %s
        """

        cursor.execute(query, (user_id,))
        expenses = cursor.fetchall()

        print("\nYour Expenses")
        print("-" * 70)
        print(f"{'ID':<5}{'Category':<15}{'Amount':<12}{'Description':<20}{'Date'}")
        print("-" * 70)

        for expense in expenses:
            print(f"{expense[0]:<5}{expense[1]:<15}₹{expense[2]:<10}{expense[3]:<20}{expense[4]}\n")

        try:
            del_id = int(input("Enter the id of the expense which yo want to delete: "))

            del_query = """
                        DELETE FROM expenses 
                        WHERE expense_id = %s
                        and user_id =%s
                        """
            cursor.execute(del_query,(del_id,user_id))
            conn.commit()
            print(f"The expense deleted Successfully..")

        except ValueError:
            print("Invalid Input....")

        except Exception as e:
            print("Unepected error ",e)



# Total Expense function
def totoal_expense(user_id):
    pass






# The main expense tarctor menu
def expense_menu(user_id):
    print("-------- Expense Tracker --------")
    print("1. Add Expense.")
    print("2. View Expense.")
    print("3. Delete Expense.")
    print("4. Totoal Expanse.")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(user_id)

        elif choice == "2":
            view_expense(user_id)

        elif choice == "3":
            delete_expnse(user_id)

        elif choice == "4":
            totoal_expense(user_id)
        
        elif choice == "5":
            print("Exited...")
            break
        else:
            print("INVALID INPUT..")
            break
        


print("-------WELCOME TO THE EXPENSE TRACKER-------")
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


