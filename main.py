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

        #Review Table
        review_col = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                        "review TEXT",
                        "userName TEXT",
                        "userNameREA TEXT"]
        
        sample_db.create_table("Review", review_col)
        
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

        review_phrases = {
            1: "Great agent, highly recommend!",
            2: "Terrible agent, would not ask this agent to sell my property again",
            3: "Terrible agent, would not buy property again from this agent",
            4: "Agent was friendly and cool!",
            5: "Average agent"
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
        def addReview(review, tuple_s, tuple_r, review_tuple):
            #List of usernames for sellers and buyers
            user_s_list = [seller[1] for seller in tuple_s]
            user_r_list = [agent[1] for agent in tuple_r]

            # Check for unique pairs and add the review
            for user_s in user_s_list:
                for user_r in user_r_list:
                    if not any(r[2] == user_s and r[3] == user_r for r in review_tuple):
                        # Insert the review into the database
                        sample_db.insert_into_table("Review", f"NULL, '{review}', '{user_s}', '{user_r}'")
                        return True  # Exit the loop once a review is added
            
            # If no unique pair is found, return False
            return False

        #Populate the REVIEW table
        for i in range(101):

            #Generate a random review
            review_og = generate_random_review()

            #Get the review key
            review_key = int(review_og[0])

            length_review_og = len(review_og)

            #Get the review
            review_string = review_og[2: length_review_og]

            #Tuple records of same review in database
            tuple_review = sample_db.search_by_keyword("Review", review_string, ["review"])

            #Search buyer
            search_result_buyer = sample_db.search_by_keyword("User", 3, ["role"])

            #Search REAs
            search_result_agent = sample_db.search_by_keyword("User", 2, ["role"])

            #Search seller
            search_result_seller = sample_db.search_by_keyword("User", 4, ["role"])

            #If it is the first entry
            if(i == 0):
                #If it is a review by SELLER
                if(review_key == 2):

                    #Get the first tuple
                    tuple_seller = search_result_seller[0]

                    #Get the username SELLER
                    username_seller = tuple_seller[1]

                    #Get the first tuple REA
                    tuple_REA = search_result_agent[0]

                    #Get AGENT username
                    username_agent = tuple_REA[1]

                    #Insert into DB
                    sample_db.insert_into_table("Review", f"NULL, '{review_string}', '{username_seller}', '{username_agent}'")

                else:
                    #Get the first tuple
                    tuple_buyer = search_result_buyer[0]

                    #Get the username BUYER
                    username_buyer = tuple_buyer[1]

                    #Get the first tuple REA
                    tuple_REA = search_result_agent[0]

                    #Get AGENT username
                    username_agent = tuple_REA[1]

                    #Insert into DB
                    sample_db.insert_into_table("Review", f"NULL, '{review_string}', '{username_buyer}', '{username_agent}'")

            #If it's not the first entry, needa to check for duplicates
            else:
                #If it is a review by seller
                if(review_key == 2):
                    addReview(review_string ,search_result_seller, search_result_agent, tuple_review)
                                

                #If it is a review by buyer
                elif(review_key == 3):
                    addReview(review_string ,search_result_buyer, search_result_agent, tuple_review)

                #If it is a review that can be made by both seller or buyer
                else:
                    noUnique = addReview(review_string ,search_result_seller, search_result_agent, tuple_review)

                    #If no unique records for seller, then check for buyer 
                    if(noUnique == False):
                        addReview(review_string, search_result_buyer, search_result_agent, tuple_review)

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

        desc_dict = {
            1: "Spacious 3-bedroom family house with a backyard garden, located in a quiet neighborhood.",
            2: "Cozy 2-bedroom apartment in the heart of downtown, with modern amenities and a city view.",
            3: "Luxurious 5-bedroom villa with a swimming pool and panoramic ocean views, perfect for entertaining guests.",
            4: "Charming 4-bedroom cottage nestled in the countryside, surrounded by lush greenery and scenic views.",
            5: "Contemporary loft-style apartment featuring an open floor plan, high ceilings, and plenty of natural light."
        }


        for i in range(1, 101):
            p_name = f"property {i}"
            location = loc_dict[random.randint(1,4)]
            description = desc_dict[random.randint(1,5)]
            img_name = f"{random.randint(1,5)}.png"
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
    # db =  database.Database("SampleDatabase")
    # print(db.search_one("User", "username = 'admin'"))
    # print("Database Initliaised!")
    # db.view_table("User")
    # db.view_table("Property")
    #print(randomReview)
    #print(len(randomReview))
    #print(randomReview[2: len(randomReview)])
    

    # db.view_table("Profile")
    # db.view_table("Review")
    # db.connection.close()

    

    # Initialise Web App
    print("--- Running App ---")
    main_app = app.WebApp(8000)
    main_app.run_app()