# Main Program (main.py)

import os.path
import sqlite3
import random
import string
from database import Database

import app
from admin import SystemAdmin

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_email(domain="example.com"):
    """Generate a random email address."""
    username = generate_random_string(8)  # Generate random username
    email = f"{username}@{domain}"
    return email


if __name__ == "__main__":
    if not os.path.exists('SampleDatabase.db'):
        # Initialise new table
        sample_db = Database("SampleDatabase")

        # User Table
        user_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT",
                            "email TEXT",
                            "role INTEGER"]
        sample_db.create_table("User", user_col)
        

        # Populating the each table with at least 100 rows to each data type
        for i in range(100):
            username = f"user{i+1}"  # Generate usernames like user1, user2, ...
            password = generate_random_string(10)  # Generate random password
            email = generate_random_email()
            role = random.randint(1, 4)  # 1 = admin, 2 = rea, 3 = buyer, 4 = seller
            sample_db.insert_into_table("User", [f"{i+1}, '{username}', '{password}',  '{email}', {role}"])
        sample_db.insert_into_table("User", ["0, 'admin', '123', 'admin@example.com', 1"])
        sample_db.insert_into_table("User", ["101, 'admin1', '123', 'admin1@example.com', 1"]) 
        sample_db.view_table("User")


    # Main Function Logic

    # Establish connection to Sample Database
    connection = sqlite3.connect('SampleDatabase.db')

    # Cursor to navigate connection
    cursor = connection.cursor()

    # Read all the tables, and create relevant objects for each row
    cursor.execute("SELECT * FROM User")
    rows = cursor.fetchall()
    user_lst= []
    for u in rows:
        if u[4] == 1:
            user_lst.append(SystemAdmin(u[0], u[1], u[2], u[3]))
        elif u[4] == 2:
            pass
        elif u[4] == 3:
            pass
        elif u[4] == 4:
            pass

    for i in user_lst:
        print(i.get_details())

    main_app = app.WebApp(8000, user_lst)
    main_app.run_app()