# Database Class (database.py)
import sqlite3

class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(f'{db_name}.db', check_same_thread=False)
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

    def search_one(self, table_name,  search_param):
        query = f"SELECT * FROM {table_name} WHERE {search_param}"
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def get_highest_id(self, table_name, id_coulmn = 'id'):
        """Get the highest ID number from a table."""
        query = f"SELECT MAX({id_coulmn}) FROM {table_name}"
        self.cursor.execute(query)
        highest_id = self.cursor.fetchone()[0]
        return highest_id if highest_id is not None else 0