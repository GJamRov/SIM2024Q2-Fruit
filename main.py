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

    # When Database hasnt been created
    if not os.path.exists('SampleDatabase.db'):
        # Create new database
        sample_db = database.Database("SampleDatabase")

        #Search for roles
        #e.g. user_dict[1] -> [1, 2, 3]
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
            role = random.randint(3, 4)  # 1 = admin, 2 = rea, 3 = buyer, 4 = seller
            active = random.randint(1, 2) # 1 = active, 2 = suspended

            #Need to have at least 50 REA to have 100 reviews and ratings
            if(i < 10):
                sample_db.insert_into_table("User", f"NULL, '{username}', '{password}',  '{email}', {1}, {active}")
                user_dict[1].append(i+1)

            elif(i > 10 and i < 51):
                sample_db.insert_into_table("User", f"NULL, '{username}', '{password}',  '{email}', {2}, {active}")
                user_dict[2].append(i+1)

            else:
                sample_db.insert_into_table("User", f"NULL, '{username}', '{password}',  '{email}', {role}, {active}")
                user_dict[role].append(i+1)
        
        # Actor accounts for test case use
        sample_db.insert_into_table("User", "0, 'admin', '123', 'admin@example.com', 1, 1")
        user_dict[1].append(0)
        sample_db.insert_into_table("User", "201, 'admin1', '123', 'admin1@example.com', 1, 2")
        user_dict[1].append(201)
        sample_db.insert_into_table("User", "202, 'rea', '123', 'rea@example.com', 2, 1")
        user_dict[2].append(202)
        sample_db.insert_into_table("User", "203, 'buyer', '123', 'buyer@example.com', 3, 1")
        user_dict[3].append(203)
        sample_db.insert_into_table("User", "204, 'seller', '123', 'seller@example.com', 4, 1")
        user_dict[4].append(204)

        #Review & Rating Table
        review_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                        "review TEXT",
                        "userName TEXT",
                        "userNameREA TEXT",
                        "actorRole INTEGER"]
        
        sample_db.create_table("Review", review_col)

        rating_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                        "rating INTEGER",
                        "userName TEXT",
                        "userNameREA TEXT",
                        "actorRole INTEGER",
                        "review_id INTEGER"]
        
        sample_db.create_table("Rating", rating_col)

        #An array of reviews to be randomly generated
        review_phrases = {
            1: "Terrible agent, would not work with this agent again",
            2: "Amazing agent, would definitely work with this agent again",
            3: "Great agent, highly recommend!",
            4: "Agent was friendly and cool!",
            5: "Average agent"
        }

        rating_phrases = {
            1: 1,
            2: 5,
            3: 4,
            4: 3,
            5: 2
        }
        
        #Function to randomly generate a review
        def generate_random_review():
            reviewNum = random.randint(1, 5)
            review = review_phrases[reviewNum]
            review_and_num = str(reviewNum) + " " + review
            return review_and_num
        
        #Function to check for duplicate reviews
        def check_duplicate_review(review_tuples, username_s, username_r):
            length_tuple = len(review_tuples)
            
            for i in range(length_tuple):
                current_tuple = review_tuples[i]
                seller_user = current_tuple[2]
                agent_user = current_tuple[3]

                if((seller_user == username_s) and (agent_user == username_r)):
                    return False
                else:
                    return True
                
        #Function to add review to table
        def addReviewRating(tuple_u, tuple_r):
            hasReviews = False
            length_u, length_r = len(tuple_u), len(tuple_r)

            random_review = generate_random_review()
            length_review = len(random_review)
            review_index = int(random_review[0])
            review = random_review[2: length_review]
            rating = rating_phrases[review_index]
            
            rea_index = random.randint(0, (length_r - 1))
            user_index = random.randint(0, (length_u - 1))

            current_user_tuple = tuple_u[user_index]
            current_rea_tuple = tuple_r[rea_index]

            current_user = current_user_tuple[1]
            current_rea = current_rea_tuple[1]
            current_role = current_user_tuple[4]

            sample_db.insert_into_table("Review", f"NULL, '{review}', '{current_user}', '{current_rea}', {current_role}")

            new_review_tuple = sample_db.search_by_keyword("Review", review, ['review'])
            review_index = 0

            for reviews in new_review_tuple:
                if reviews[2] == current_user and reviews[3] == current_rea:
                    review_index = reviews[0]
            sample_db.insert_into_table("Rating", f"NULL, {rating}, '{current_user}', '{current_rea}', {current_role}, {review_index}")

        counter = 0
        #Populate the REVIEW and RATING table
        for i in range(101):
            random_int = random.randint(1, 2)
            user_tuple = ""
            rea_tuple = sample_db.search_by_keyword("User", 2, ["role"])

            if(random_int == 1):
                user_tuple = sample_db.search_by_keyword("User", 3, ["role"])   
            else:
                user_tuple = sample_db.search_by_keyword("User", 4, ["role"])

            addReviewRating(user_tuple, rea_tuple)

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
            seller_id = random.choice(user_dict[4])
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
                            "description TEXT",
                            "active INTEGER"] 
        sample_db.create_table("Profile", profile_col)
        sample_db.insert_into_table("Profile", f"1, 'System Admin', 'FruitRealEstate system admin', 1")

        #print(user_dict[2])

    ## When database is already populated
    db = database.Database("SampleDatabase")

    test_r = set()
    for review in db.view_table("Review"):
        test_r.add(review[3])
    print(test_r)
    # db.connection.close()
    test_p = []
    for property in db.view_table("Property"):
        test_p.append(property[6])

    test_sellers = []
    for seller in test_p:
        t_seller = db.search_by_keyword("User", seller, ["id"])[0]
        test_sellers.append(t_seller)
    # print(test_p)
    print("SELLER WITH PROPERTIES:", test_sellers[0])

    # print(db.view_table("Favourite"))
    user_with_favs = []
    for f_user in db.view_table("Favourite"):
        user_with_favs.append(db.search_one("User", f"id = {f_user[1]}"))
    print("BUYER WITH FAVS:", user_with_favs[0])

    # Initialise Web App
    print("--- Running App ---")
    main_app = app.WebApp(8000)
    main_app.run_app()