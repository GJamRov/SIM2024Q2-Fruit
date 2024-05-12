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
        user_dict = {1: [], 2: [], 3: [], 4: []}

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
            # add row to user_dict
            user_dict[role].append(i+1)
            sample_db.insert_into_table("User", f"NULL, '{username}', '{password}',  '{email}', {role}, {active}")
        
        # Actor accounts for test case use
        sample_db.insert_into_table("User", "0, 'admin', '123', 'admin@example.com', 1, 1")
        sample_db.insert_into_table("User", "101, 'admin1', '123', 'admin1@example.com', 1, 2")
        sample_db.insert_into_table("User", "102, 'rea', '123', 'rea@example.com', 2, 1")
        sample_db.insert_into_table("User", "103, 'buyer', '123', 'buyer@example.com', 3, 1")
        sample_db.insert_into_table("User", "104, 'seller', '123', 'seller@example.com', 4, 1")
        #sample_db.view_table("User")
        print(sample_db.search_one("User", "username = 'admin'"))

        # Propety Listing Table
        property_listing_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                                "name TEXT",
                                "location TEXT",
                                "description TEXT",
                                "img TEXT",
                                "price INTEGER",
                                "rea_id INTEGER",
                                "seller_id INTEGER",
                                "buyer_id INTEGER",
                                "view_count INTEGER",
                                "wishlisted INTEGER"]
        sample_db.create_table("Property", property_listing_col)

        loc_dict = {
            1: "North Town",
            2: "South City",
            3: "East Village",
            4: "West Coast"
        }

        p_name_dict = {
            1: "White Bungalow with Pool",
            2: "Modern House with Pool",
            3: "3-Bedroom City-Centre Condominium",
            4: "4-Bedroom Town Condominium",
            5: "4-Bedroom Modern City Aparment",
            6: "5-Bedroom Town Apartment"
        }

        p_img_dict = {
            1: "house1.png",
            2: "house2.webp",
            3: "house3.webp",
            4: "house4.jpeg",
            5: "house5.jpeg",
            6: "house6.jpeg"
        }

        desc_dict = {
            1: "This beautiful white bungalow offers a peaceful retreat with a private pool and spacious backyard garden, perfect for family gatherings and relaxation. The interior features a modern design with open living spaces and ample natural light, creating a welcoming atmosphere for residents.",
            2: "Experience urban living at its finest in this modern house located in a vibrant neighborhood. With a refreshing pool and contemporary amenities, this home provides both comfort and style. Enjoy panoramic city views from the rooftop terrace, ideal for entertaining guests or unwinding after a busy day.",
            3: "Elegance meets convenience in this stunning 3-bedroom condominium situated in the heart of the city center. Featuring luxurious amenities, including a pool and fitness center, this residence offers a sophisticated urban lifestyle. The spacious layout and modern finishes make it an ideal choice for discerning homeowners.",
            4: "Discover the charm of this 4-bedroom townhouse-style condominium, offering a perfect blend of comfort and community living. With well-appointed interiors and a shared courtyard, this home provides a cozy retreat in a bustling urban setting. Experience modern conveniences and a sense of community in this desirable residence.",
            5: "Step into luxury with this exquisite 4-bedroom modern city apartment boasting contemporary design elements and expansive living spaces. Enjoy breathtaking city views from the private balcony and entertain guests in style with the gourmet kitchen and elegant dining area. This residence offers a sophisticated urban lifestyle.",
            6: "Experience the epitome of luxury living in this spacious 5-bedroom town apartment, offering unparalleled comfort and style. With high-end finishes, private outdoor spaces, and panoramic views, this home is perfect for those seeking a premium urban lifestyle in a desirable location."
        }


        for i in range(1, 101):
            house_choice = random.randint(1,6)
            p_name = p_name_dict[house_choice]
            location = loc_dict[random.randint(1,4)]
            description = desc_dict[house_choice]
            img_name = p_img_dict[house_choice]
            price = random.randint(50000, 1000000)
            rea_id = random.choice(user_dict[2])
            seller_id = random.choice(user_dict[3])
            sold_buyer = -1
            view_count = random.randint(1, 9999)
            wishlisted = random.randint(1, 9999)
            sample_db.insert_into_table("Property", f"NULL, '{p_name}', '{location}', '{description}', '{img_name}', {price}, {rea_id}, {seller_id}, {sold_buyer}, {view_count}, {wishlisted}")

        # Favourite Table Schema
        favourite_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                        "user_id INTEGER",
                        "property_id INTEGER"]
        sample_db.create_table("Favourite", favourite_col)

        for i in range(1,101):
            fav_chance = random.randint(1, 10)
            if fav_chance == 1:
                b_id = random.choice(user_dict[3])
                sample_db.insert_into_table("Favourite", f"NULL, '{b_id}', '{i}'")

        # Profile Table
        profile_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                            "type TEXT",
                            "description TEXT",] 
        sample_db.create_table("Profile", profile_col)
        sample_db.insert_into_table("Profile", f"1, 'System Admin', 'FruitRealEstate system admin'")
        
    ## When database is already populated
    db =  database.Database("SampleDatabase")
    # print(db.search_one("User", "username = 'admin'"))
    # print("Database Initliaised!")
    # db.view_table("User")
    # db.view_table("Property")
    # db.view_table("Profile")
    db.connection.close()

    # Initialise Web App
    print("--- Running App ---")
    main_app = app.WebApp(8000)
    main_app.run_app()