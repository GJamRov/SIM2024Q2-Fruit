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
        
    def insert_into_table(self, table_name:str, values:str):
        query = f"INSERT INTO {table_name} VALUES ({values})"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def view_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        print(rows)
        return rows
    
    def update_table(self, table_name, set_values, condition):
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def search_one(self, table_name,  search_param):
        query = f"SELECT * FROM {table_name} WHERE {search_param}"
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def search_by_keyword(self, table_name, keyword, search_columns):
        """Search for records in a table based on a keyword."""
        # Sample usage search_results = sample_db.search_by_keyword("User", "admin", ["username", "email"])
        # Constructing the WHERE clause for search_columns
        where_clause = " OR ".join([f"{column} LIKE ?" for column in search_columns])
        query = f"SELECT * FROM {table_name} WHERE {where_clause}"

        # Adding '%' wildcard to the keyword for pattern matching
        keyword_with_wildcard = f"%{keyword}%"

        self.cursor.execute(query, [keyword_with_wildcard] * len(search_columns))
        rows = self.cursor.fetchall()
        print(rows)
        return rows
    
    def delete_from_table(self, table_name, condition):
        """Delete records from a table based on a condition."""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Deleted rows from {table_name} where {condition}")
    
    def get_highest_id(self, table_name, id_coulmn = 'id'):
        """Get the highest ID number from a table."""
        query = f"SELECT MAX({id_coulmn}) FROM {table_name}"
        self.cursor.execute(query)
        highest_id = self.cursor.fetchone()[0]
        return highest_id if highest_id is not None else 0
    