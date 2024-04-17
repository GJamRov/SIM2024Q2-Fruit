import sqlite3
# Code to initialise database

# Establish connection to database
connection = sqlite3.connect('sampleDatabase.db')

# Cursor to navigate connection
cursor = connection.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS SystemAdmins (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
)
""")

# TODO: Code to populate the SystemAdmins table
#cursor.execute("""
#INSERT INTO SystemAdmins VALUES
#(1, 'Paul', 'Smith'),
#(2, 'Mark', 'Jacobs'),
#(3, 'Anna', 'Smith')
#""")

connection.commit()
connection.close()