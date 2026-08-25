# Expense Tracker

A command-line based **Expense Tracker** built with **Python** and **MySQL**. This application allows multiple users to register, log in securely, and manage their personal expenses. Each user's expenses are stored separately using a relational database with a foreign key relationship.

---

# Features

* User Registration
* User Login
* Add Expense
* View Expenses
* Delete Expense
* Calculate Total Expenses
* Multi-user Support
* MySQL Database Integration
* Exception Handling

---

# Technologies Used

* Python 3
* MySQL
* mysql-connector-python

---

# Project Structure

```text
Expense-Tracker/
│
├── main.py          # Main application logic
├── database.py      # Database connection
├── README.md

# Database Schema

## Users Table

```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
```

## Expenses Table

```sql
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category VARCHAR(100),
    amount DECIMAL(10,2),
    description VARCHAR(255),
    expense_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/shubhamjadha04/Expense-Tracker.git
```

## 2. Navigate to the project directory

```bash
cd Expense-Tracker
```

## 3. Install dependencies

```bash
pip install mysql-connector-python
```

## 4. Create the MySQL database

Create a database and execute the SQL queries provided above to create the required tables.

---

# Running the Project

Run the application using:

```bash
python main.py
```

---

# Application Flow

```text
Start
   │
   ▼
Register / Login
   │
   ▼
Expense Menu
   │
   ├── Add Expense
   ├── View Expenses
   ├── Delete Expense
   ├── Total Expenses
   └── Exit
```

---

# Current Features

### Register User

Creates a new account with a unique email address.

### Login User

Authenticates the user using email and password.

### Add Expense

Stores a new expense with:

* Category
* Amount
* Description
* Date & Time

### View Expenses

Displays all expenses belonging to the logged-in user.

### Delete Expense

Allows the user to delete a specific expense by selecting its Expense ID.

### Total Expense

Calculates the total amount spent by the logged-in user using SQL's `SUM()` function.

---

# Sample Output

```text
-------WELCOME TO THE EXPENSE TRACKER-------

1. Register
2. Login

Enter your choice: 2

Login Successful!

-------- Expense Tracker --------

1. Add Expense
2. View Expense
3. Delete Expense
4. Total Expense
5. Exit
```

---

# Future Improvements

* Update Expense
* Search Expenses
* Filter by Date
* Monthly Reports
* Budget Management
* Password Hashing using bcrypt
* Export to CSV
* Export to PDF
* Data Visualization using Matplotlib
* Flask Web Application
* Dashboard

---

# Learning Outcomes

This project helped me learn:

* Python Functions
* MySQL CRUD Operations
* Relational Database Design
* Foreign Keys
* Parameterized SQL Queries
* Exception Handling
* Database Connectivity using mysql-connector
* User Authentication
* CLI Application Development

---

# Author

**Shubham Jadhao**

GitHub: https://github.com/shubhamjadha04

---

# License

This project is created for learning purposes and personal portfolio development.
