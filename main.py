import os.path
import sqlite3
import random
import string
from database import Database

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

if __name__ == "__main__":
    if not os.path.exists('SampleDatabase.db'):
        # Initialise new table
        sample_db = Database("SampleDatabase")

        # User Table
        user_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT",
                            "role INTEGER"]
        sample_db.create_table("User", user_col)
        

        # Populating the each table with at least 100 rows to each data type
        for i in range(100):
            username = f"user{i+1}"  # Generate usernames like user1, user2, ...
            password = generate_random_string(10)  # Generate random password
            role = random.randint(1, 3)  # Assign a random role (1, 2, or 3)
            sample_db.insert_into_table("User", [f"{i+1}, '{username}', '{password}', {role}"])
        sample_db.view_table("User")


    # TODO: Main Function Logic

    # Establish connection to Sample Database
    connection = sqlite3.connect('SampleDatabase.db')

    # Cursor to navigate connection
    cursor = connection.cursor()

    # Read all the tables, and create relevant objects for each row
    cursor.execute("SELECT * FROM User")
    rows = cursor.fetchall()
    print(rows)