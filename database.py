# Database Class (database.py)
import sqlite3
from entity.user import User
from entity.admin import SystemAdmin
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect('SampleDatabase.db')
        self.cursor = self.connection.cursor()
        self.users = []
        self.listings = []
    
    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} "
        column_text = ", ".join(columns)
        query += f"({column_text})"
        self.cursor.execute(query)
        self.connection.commit()
        
    def insert_into_table(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES"
        value_q = ", ".join(values)
        query += f"({value_q})"
        self.cursor.execute(query)
        self.connection.commit()

    def view_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        print(rows)
    
    def update_table(self, table_name, set_values, condition):
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def init_users(self):
        # Read all the tables, and create relevant objects for each row
        self.cursor.execute("SELECT * FROM User")
        rows = self.cursor.fetchall()
        for u in rows:
            if u[4] == 1: # System Admin
                self.users.append(SystemAdmin(u[0], u[1], u[2], u[3], u[4]))
            elif u[4] == 2: # REA
                self.users.append(REA(u[0], u[1], u[2], u[3], u[4]))
            elif u[4] == 3: # Buyer
                self.users.append(Buyer(u[0], u[1], u[2], u[3], u[4]))
            elif u[4] == 4: # Seller
                self.users.append(Seller(u[0], u[1], u[2], u[3], u[4]))