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

        ## Real Estate Agent Tables
        rea_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT"]
        sample_db.create_table("RealEstateAgent", rea_col)

        ## Buyer Tables
        buyer_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT"]
        sample_db.create_table("Buyer", buyer_col)

        ## Seller Tables
        seller_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "password TEXT"]
        sample_db.create_table("Seller", seller_col)

        #TODO: Populating the each table with at least 100 rows to each data type
        

    # TODO: Main Function Logic

    # Establish connection to Sample Database
    connection = sqlite3.connect('SampleDatabase.db')

    # Cursor to navigate connection
    cursor = connection.cursor()