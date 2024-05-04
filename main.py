# Main Program (main.py)
import os.path
import random
import string
import database
import app

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
    # print(os.path.exists("SampleDatabase.db"))
    # When Database hasnt been created
    if not os.path.exists('SampleDatabase.db'):
        # Create new database
        sample_db = database.Database("SampleDatabase")

        # User Table
        user_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                            "username TEXT",
                            "password TEXT",
                            "email TEXT",
                            "role INTEGER",
                            "active INTEGER"]
        sample_db.create_table("User", user_col)
        
        # Populating the each table with at least 100 rows to each data type
        for i in range(100):
            username = f"user{i+1}"  # Generate usernames like user1, user2, ...
            password = generate_random_string(10)  # Generate random password
            email = generate_random_email()
            role = random.randint(1, 4)  # 1 = admin, 2 = rea, 3 = buyer, 4 = seller
            active = random.randint(1, 2) # 1 = active, 2 = suspended
            sample_db.insert_into_table("User", [f"NULL, '{username}', '{password}',  '{email}', {role}, {active}"])
        
        # Actor accounts for test case use
        sample_db.insert_into_table("User", ["0, 'admin', '123', 'admin@example.com', 1, 1"])
        sample_db.insert_into_table("User", ["101, 'admin1', '123', 'admin1@example.com', 1, 2"])
        sample_db.insert_into_table("User", ["102, 'rea', '123', 'rea@example.com', 2, 1"])
        sample_db.insert_into_table("User", ["103, 'buyer', '123', 'buyer@example.com', 3, 1"])
        sample_db.insert_into_table("User", ["104, 'seller', '123', 'seller@example.com', 4, 1"])
        sample_db.view_table("User")
        print(sample_db.search_one("User", "username = 'admin'"))

        # Propety Listing Table
        property_listing_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                                "name TEXT",
                                "price INTEGER",
                                "view_count INTEGER",
                                "wishlisted INTEGER"]
        sample_db.create_table("Property", property_listing_col)

        for i in range(1, 101):
            p_name = f"property {i}"
            price = random.randint(50000, 1000000)
            view_count = random.randint(1, 9999)
            wishlisted = random.randint(1, 9999)
            sample_db.insert_into_table("Property", [f"NULL, '{p_name}', {price}, {view_count}, {wishlisted}"])

        # Profile Table
        profile_col = ["id INTEGER PRIMARY KEY",
                            "username TEXT",
                            "name TEXT",
                            "type TEXT",
                            "description TEXT",]
        
        sample_db.create_table("Profile", profile_col)
        
    ## When database is already populated
    db =  database.Database("SampleDatabase")
    # print(db.search_one("User", "username = 'admin'"))
    # print("Database Initliaised!")
    db.view_table("User")
    db.view_table("Property")
    db.connection.close()

    # Initialise Web App
    print("--- Running App ---")
    main_app = app.WebApp(8000)
    main_app.run_app()