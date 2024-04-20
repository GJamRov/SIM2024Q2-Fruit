import sqlite3

class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect('SampleDatabase.db')
        self.cursor = self.connection.cursor()
    
    def  create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} "
        column_text = ", ".join(columns)
        query += f"({column_text})"
        self.cursor.execute()
        self.connection.commit()
        
    def insert_into_table(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES"
        value_q = ", ".join(values)
        query += f"({value_q})"
        self.cursor.execute()
        self.connection.commit()

# TODO: Code to populate the SystemAdmins table
#cursor.execute("""
#INSERT INTO SystemAdmins VALUES
#(1, 'Paul', 'Smith'),
#(2, 'Mark', 'Jacobs'),
#(3, 'Anna', 'Smith')
#""")

