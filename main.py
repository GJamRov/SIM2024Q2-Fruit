import os.path
import sqlite3
from database import Database

if __name__ == "__main__":
    if not os.path.exists('SampleDatabase.db'):
        sample_db = Database("SampleDatabase")
        system_admin_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT"]
        sample_db.create_table("SystemAdmins", system_admin_col)
        #TODO: Populating the System Admins table with 100 entries of data
        

    # TODO: Main Function Logic

    # Establish connection to Sample Database
    connection = sqlite3.connect('SampleDatabase.db')

    # Cursor to navigate connection
    cursor = connection.cursor()