from flask import Flask, Blueprint, render_template, request, redirect, session, flash, url_for, jsonify
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

# Controller Imports
from controllers.login import LoginController
from controllers.createAccount import createAccountController
from controllers.viewAccount import viewAccountController
from controllers.updateAccount import updateAccountController
from controllers.suspendAccount import suspendAccountController
from controllers.reactivateAccount import reactivateUserAccountController
from controllers.createProfile import createUserProfileController
from controllers.viewProfile import viewUserProfileController
from controllers.updateProfile import updateUserProfileController
from controllers.suspendProfile import suspendUserProfileController
from controllers.reactivateProfile import reactivateUserProfileController
from controllers.viewPropertyListing import viewPLController
from controllers.createPropertyListing import createPLController
from controllers.viewReview import viewReviewController
from controllers.viewRating import viewRatingController
from controllers.editReview import editReviewController
from controllers.giveReview import giveReviewController
from controllers.giveRating import giveRatingController
from controllers.editReview import editReviewController
from controllers.editRating import editRatingController

# Entity Import
from entity.user import User

class WebApp:

    def __init__(self, port):
        self.app = Flask(__name__)
        self.upload_folder = os.path.normpath(os.path.dirname(os.path.abspath(__file__))) + "\static"
        self.port = port
        self.app.secret_key = 'super secret key'  # for sessions
        self.blueprint = Blueprint('web_app', __name__)
        self.app.before_request(self.check_authentication)

    def set_port(self, port: int):
        self.port = port

    def check_authentication(self):
        """Check if the user is authenticated."""
        # Exclude routes that should be accessible without authentication
        # print(request.endpoint)
        excluded_routes = ['/login', 'static', 'web_app.login']
        if request.endpoint and not any(request.endpoint.startswith(exclude) for exclude in excluded_routes):
            if not session.get('logged_in'):
                return redirect('/login')

    def run_app(self):
        """Runs the web application."""
        self.app.config['UPLOAD_FOLDER'] = self.upload_folder
        self.app.config['SESSION_TYPE'] = 'redis'
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)
        
        # Default Pages
        self.blueprint.add_url_rule('/', 'home', self.home)
        self.blueprint.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout', 'logout', self.logout, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/profile/<username>', 'profile', self.profile, methods=['GET', 'POST'])

        # User Account Pages
        self.blueprint.add_url_rule('/users/', 'users_index', self.users_index, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/create', 'create_account', self.create_account, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/view/<account>', 'view_account', self.view_account, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/update/<account>', 'update_account', self.update_account, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/suspend/<account>', 'suspend_account', self.suspend_account, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/reactivate/<account>', 'reactivate_account', self.reactivate_account, methods=['GET', 'POST'])
        # user profile pages
        self.blueprint.add_url_rule('/user-profiles/', 'user_profiles_index', self.user_profiles_index, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/create', 'create_profile', self.create_profile, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/view/<profile>', 'view_profile', self.view_profile, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/update/<profile>', 'update_profile', self.update_profile, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/suspend/<profile>', 'suspend_profile', self.suspend_profile, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/reactivate/<profile>', 'reactivate_profile', self.reactivate_profile, methods=['GET', 'POST'])
        # property listing pages
        self.blueprint.add_url_rule('/property-listings/', 'property_listings_index', self.property_listings_index)
        self.blueprint.add_url_rule('/property-listings/sort', 'property_listings_sort', self.property_listings_sort)
        self.blueprint.add_url_rule('/property-listings/view', 'property_listings_view', self.property_listings_view)
        self.blueprint.add_url_rule('/property-listings/create', 'property_listings_create', self.property_listings_create, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/property-listings/update', 'property_listings_update', self.property_listings_update)
        self.blueprint.add_url_rule('/upload', 'upload_file', self.upload_file, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/add_to_wishlist/<int:listing_id>', view_func=self.add_to_wishlist, methods=['POST'])

        # my profile
        self.blueprint.add_url_rule('/my-profile/', 'my_profile_index', self.my_profile_index)
        self.blueprint.add_url_rule('/my-profile/view', 'my_profile_view', self.my_profile_view)

        # reviews
        self.blueprint.add_url_rule('/reviews/', 'reviews_index', self.reviews_index)

        # wishlists
        self.blueprint.add_url_rule('/wishlists/', 'wishlists_index', self.wishlists_index)

        # my reviews - for buyers and sellers
        self.blueprint.add_url_rule('/my-reviews/', 'my_reviews_index', self.my_reviews_index)
        self.blueprint.add_url_rule('/my-reviews/create', 'my_reviews_create', self.my_reviews_create, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/my-reviews/update', 'my_reviews_update', self.my_reviews_update, methods=['GET', 'POST'])

        self.app.register_blueprint(self.blueprint)
        User.connect_database("SampleDatabase")
        self.app.run(debug=True, port=self.port)

    def home(self):
        """View function for the view route."""
        username = session['username']
        return render_template("pages/home.html", username=username)
    
    ## User Functionalities
    def login(self):
        """User login route"""
        template = 'login.html'
        
        # Request data from web page
        if request.method == 'POST':
            entered_username = request.form['username']
            entered_password = request.form['password']

            # Login Controller handles login
            loginCtl = LoginController()
            role = loginCtl.validateLogin(entered_username, entered_password)

            #Session data assignment and page redirect on successful login
            if 0 < role < 5:
                session['username'] = entered_username
                session['role'] = role
                session['logged_in'] = True
                # flash('Login successful!', 'success')
                # return redirect(url_for('web_app.profile', username=session['username']))
                return redirect("/")
            elif role == 5:
                flash('Account is suspended', 'error')
            elif role == 6:
                flash('Invalid username or password', 'error')   
            elif role == 7:
                flash('User profile is suspended', 'error')          
        
        return render_template(template)      

    def logout(self):
        """User logout route"""

        #Clear session data and redirect to login page once logged out
        session.pop('username')
        session.pop('role')
        session.pop('logged_in', None)
        try:
            session['_flashes'].clear()
            #flash('Logout successful!', 'success')
            return redirect('/login')
        except KeyError:
            return redirect('/login')

    def profile(self, username):
        """Assign & display user profile"""

        role = session.get('role')

        try:
            #User profile assignment if successfully logged in
            if session.get('logged_in'):
                if role == 1:
                    template = 'profile_admin.html'
                elif role == 2:              
                    template = 'profile_rea.html'
                elif role == 3:          
                    template = 'profile_buyer.html'
                elif role == 4:             
                    template = 'profile_seller.html'
            else:
                #If 'logged_in' key is not found in session, redirect to login page
                return redirect('/login')
            
            return render_template(template, username=username)
        except KeyError:
            #If 'role' key is not found in session, redirect to login page
            return redirect('/login')
    
    ## System Admin Functionalities
    # 3. Create user accounts
    def create_account(self):
        """Create new user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                entered_username = request.form['username']
                entered_password = request.form['password']
                entered_confirm_password = request.form['confirm-password']
                entered_email = request.form['email']
                entered_profile = request.form['profile']

                if entered_password == entered_confirm_password:
                    # Send details to controller
                    createAccountCtl = createAccountController()
                    acc_details = [entered_username, entered_password, entered_email, entered_profile]
                    print(acc_details)
                    created = createAccountCtl.addUserAccount(acc_details)
                    if created:
                        flash("User account created successfully!", "success")
                        return redirect('/users/')
                    else:
                        flash("Error creating user account, please try again!", "error")
                        return redirect('/users/create')
            return render_template("pages/users/create.html")

    #4. View user accounts
    def view_account(self, account):
        """View user accounts"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            viewAccCtl = viewAccountController()
            account_data = viewAccCtl.viewUserAccount(account)
            if account_data:
                return render_template('pages/users/view.html', account=account_data)
            else:
                flash("Invalid user", "error")
                return redirect('/users/')
        
    #5. Update user accounts
    def update_account(self, account):
        """Update existing user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            if account == 'admin':
                flash("admin cannot be edited", "error")
                return redirect('/users/')
            # password = request.args.get('password')
            email = request.args.get('email')
            role = request.args.get('role')
            # Get form data from POST request
            if request.method == 'POST':
                updateAccountCtl = updateAccountController()
                acc_details = [request.form['account_name'], request.form['username'], request.form['password'], request.form['email'], request.form['role']]
                if updateAccountCtl.updateUserAccount(acc_details):
                    flash("Account updated successfully!", "succcess")
                    return redirect('/users/')
                else:
                    flash("Failed to update account. Please try again.", "error")
                    return redirect('/users/')
            return render_template("pages/users/update.html", account=account, email=email, role=role)
        
    #6. Suspend user account
    def suspend_account(self, account):
        """Suspend a user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            suspendAccountCtl = suspendAccountController()
            if account != 'admin':
                if suspendAccountCtl.suspendUserAccount(account):
                    flash("User account suspended!", "success")
                else:
                    flash("System admin cannot be suspended", "error")
            else:
                flash("admin cannot be suspended", "error")
            return redirect('/users/')

    # 8. Create user profiles
    def create_profile(self):
        """Create new user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                UP = [request.form['profile_type'], request.form['profile_desc']]
                createProfileCtl = createUserProfileController()
                if createProfileCtl.createUserProfile(UP):
                    flash("User profile created successfully!", "success")
                    return redirect('/user-profiles/')
                else:
                    flash("User profile already exists! Please try again", "error")
                    return redirect('/user-profiles/create')
            return render_template("pages/user-profiles/create.html")
        
    #TODO: 9. View user profiles
    def view_profile(self, profile):
        """View user profiles"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            viewProfileCtl = viewUserProfileController()
            profile_data = viewProfileCtl.viewUserProfile(profile)
            if profile_data:
                return render_template('pages/user-profiles/view.html', profile=profile_data)
            else:
                flash("Invalid user profile", "error")
                return redirect('/user-profiles/')

    #TODO: 10. Update user profiles
    def update_profile(self, profile):
        """Update user profile"""
        # Check that the user is a System Admin
        profile_desc = request.args.get('profile_desc')
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                updateProfileCtl = updateUserProfileController()
                if updateProfileCtl.updateUserProfile(request.form['profile_name'], request.form['profile_desc']):
                    flash("Profile description updated successfully!", "success")
                    return redirect('/user-profiles/')
                else:
                    flash("Failed to update profile. Please try again.", "error")
                    return redirect('/user-profiles/update')
            return render_template('pages/user-profiles/update.html', profile=profile, profile_desc=profile_desc)

    #TODO: 11. Suspend user profile
    def suspend_profile(self, profile):
        """Suspend user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            suspendUserProfileCtl = suspendUserProfileController()
            if profile != 'System Admin':
                if suspendUserProfileCtl.suspendUserProfile(profile):
                    flash("User profile suspended!", "success")
                else:
                    flash("Error suspending user profile", "error")
            else:
                flash("System Admin cannot be suspended", "error")
            return redirect('/user-profiles/')
        
    #TODO: 13. Reactivate user account
    def reactivate_account(self, account):
        """Reactivate user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            reactivateAccountCtl = reactivateUserAccountController()
            if reactivateAccountCtl.reactivateUserAccount(account):
                flash("User account reactivated!", "success")
            else:
                flash("Failed to reactivate user acccount. Please try again.", "error")
            return redirect('/users/')
        

    #TODO: 14. Reactivate user profile
    def reactivate_profile(self, profile):
        """Reactivate user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            reactivateUserProfileCtl = reactivateUserProfileController()
            if reactivateUserProfileCtl.reactivateUserProfile(profile):
                flash("User profile reactivated!", "success")
            else:
                flash("Error reactivated user profile", "error")
            return redirect('/user-profiles/')

    # user tab
    def users_index(self):
        """users index page"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            viewAccCtl = viewAccountController()
            users = viewAccCtl.viewAllUsers()
            if users:
                return render_template("pages/users/index.html", users=users)
        return render_template("pages/users/index.html")

    # user profile tab
    def user_profiles_index(self):
        """user profile index page"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            viewProfileCtl = viewUserProfileController()
            profiles = viewProfileCtl.viewAllUserProfile()
            
            if profiles:
                return render_template("pages/user-profiles/index.html", profiles=profiles)
            return render_template("pages/user-profiles/index.html")

    # property listing
    def property_listings_index(self):
        """Main page for viewing property listings"""
        # Checks that the user is an REA, buyer or seller
        while session['role'] > 1 and session['role'] < 5:
            sort_option = request.args.get('sort')
            viewPLCtl = viewPLController()
            properties = viewPLCtl.viewListing(session['username'], "", sort_option)
            #print(properties, "RIGHT HERE")
            if properties:
                # print(properties)
                return render_template('pages/property-listings/index.html', propertyListings = properties)
            else:
                return render_template('/')
    
    def property_listings_sort(self):
        """ Handles the sorting drop down bar for view property listings"""
        sort_option = request.args.get('sort')
        # Calls controller to fetch sorted property listings
        viewPLCtl = viewPLController()
        sorted_properties = viewPLCtl.viewListing(session['username'], "", sort_option)

        # Return sorted listings as JSON response
        return jsonify(sorted_properties)

    def property_listings_view(self):
        """View a property listing"""
        viewPLCtl = viewPLController()
        listing_id = request.args.get("listing_id")
        listing = viewPLCtl.viewListing(session['username'], listing_id)
        print(listing, "LISTING HERE")
        if listing:
            return render_template("pages/property-listings/view.html", listing=listing)
        else:
            flash('Listing not found', 'error')
            return redirect(url_for('web_app.property_listings_index'))

    def property_listings_create(self):
        """Create a property listing"""
        if session['role'] == 2:
            return render_template("pages/property-listings/create.html")
        else:
            flash('You do not have permission to create a property listing!', 'error')
            return redirect("/")     
    
    def upload_file(self):
        """Handles the form submission for property_listings_create"""
        if 'image' in request.files:
            image_file = request.files['image']
            name = request.form['location']
            location = request.form['location']
            price = request.form['price']

            # Save the image file to UPLOAD_FOLDER
            image_filename = secure_filename(image_file.filename)
            image_filepath = os.path.normpath(os.path.join(self.app.config['UPLOAD_FOLDER'], image_filename)) 
            image_file.save(image_filepath)

            # Save new property details to database
            createPLCtl = createPLController()
            result = createPLCtl.createPropertyListing(session['username'], [name, location, image_filename, price])

            if result:
                flash('Property listing created successfully!', 'success')
                return redirect(url_for('web_app.property_listings_index'))
            else:
                flash('Property listing created unsuccssfully.', 'error')
                return redirect("pages/property-listings/create.html")
        return redirect('/property-listings/create')
    
    def add_to_wishlist(self, listing_id):
        data = request.json
        print(data)
        response_data = {'message': 'Property added to wishlist successfully'}
        return jsonify(response_data), 200  # Return a JSON response with a success status code

    def property_listings_update(self):
        """Update a property listing"""
        return render_template("pages/property-listings/update.html")
    
    def property_listings_delete(self):
        """Delete a property listing"""

        return redirect(url_for("web_app.my_profile_index"))

    # my profile
    def my_profile_index(self):
        """Main Page for Individual User Profile"""
        # Checks that the user is an REA, buyer or seller
        while session['role'] in [2,3,4]:
            # sort_option = request.args.get('sort')
            viewPLCtl = viewPLController()
            properties = viewPLCtl.viewListing(session['username'], propertyDetail="profile")
            # print(properties, "RIGHT HERE")
            return render_template("pages/my-profile/index.html", propertyListings = properties)
            
        return redirect("/")

    def my_profile_view(self):
        """View one of my listing"""
        viewPLCtl = viewPLController()
        listing_id = request.args.get("listing_id")
        listing = viewPLCtl.viewListing(session['username'], listing_id)
        if listing:
            return render_template("pages/my-profile/view.html", listing=listing)
        else:
            flash('Listing not found', 'error')
            return redirect(url_for('web_app.my_profile_index'))


    # reviews
    
    def reviews_index(self):
        current_role = session['role']
        
        if current_role == 1:
            flash("You do not have access", "error")
            return redirect("/")

        while session['role'] > 1 and session['role'] < 5:

            sort_option = request.args.get('sort')
            viewReviewCtl = viewReviewController()
            current_user = session['username']
            reviews = viewReviewCtl.viewReview(user_id=current_user, role=current_role)

            viewRatingCtl = viewRatingController()
            ratings = viewRatingCtl.viewRating(agent_id=current_user, role=current_role)
            if reviews:
                return render_template('pages/my-reviews/index.html', reviewListing = reviews, ratingListing = ratings, role=current_role)
            else:
                flash("No Reviews!", "error")
                return redirect("/")

    # wishlists
    def wishlists_index(self):
        """wishlists page"""
        return render_template("pages/wishlists/index.html")

    # my reviews given - for buyers and sellers
    def my_reviews_index(self):
        """my reviews page"""
        # Checks that the user is an REA, buyer or seller
        current_role = session['role']

        if current_role == 1:
            flash("ERROR 101: You DO NOT have permission to view", "error")
            return redirect("/")

        while session['role'] > 1 and session['role'] < 5:

            viewReviewCtl = viewReviewController()
            current_user = session['username']
            reviews = viewReviewCtl.viewReview(user_id=current_user, role=current_role)

            viewRatingCtl = viewRatingController()
            ratings = viewRatingCtl.viewRating(agent_id=current_user, role=current_role)
            if reviews:
                return render_template('pages/my-reviews/index.html', reviewListing = reviews, ratingListing = ratings, role=current_role)
            else:
                flash("No Reviews!", "error")
                return redirect("/")

    def my_reviews_update(self):
        """update my reviews page"""
        current_role = session['role']

        if current_role == 1 or current_role == 2:
            flash("ERROR 101: You DO NOT have permission to edit!!!", "error")
            return redirect("/")
        
        while current_role == 3 or current_role == 4:
            index = request.args.get("review_id")

            if request.method == 'POST':
                new_rating = request.form['sort']
                new_review = request.form['profile_desc']
                current_username = session['username']
                profile_name = request.form['profile_name']
                review_index = request.form['review_id']
                print(new_review)
                print(review_index)
                print(profile_name)


                updateReviewCtl = editReviewController()
                updateRatingCtl = editRatingController()
                updateReviewBool = updateReviewCtl.editReview(review_index, new_review, current_username, current_role)
                updateRatingBool = updateRatingCtl.editRating(review_index, new_rating, current_username, current_role, new_review)

                if(updateReviewBool == True and updateRatingBool == True):
                    flash("Successfully edited!", "success")
                    return redirect(url_for('web_app.my_reviews_index'))
                else:
                    flash("Error", "error")
                    return redirect(url_for('web_app.my_reviews_index'))
        
            return render_template("pages/my-reviews/update.html", profile=session['username'], review_id=index)
        return redirect("/")
    
    def my_reviews_create(self):
        """create reviews page"""
        current_role = session['role']

        if(current_role == 1 or current_role == 2):
            flash("ERROR 101: You DO NOT have permission to create reviews")
            return redirect("/")
        
        while current_role == 3 or current_role == 4:
            current_user = session['username']

            if request.method == 'POST':
                new_review = request.form['profile_desc']
                new_rating = request.form['sort']
                agent_profile = request.form['userNameREA']
                
                giveReviewCtl = giveReviewController()
                giveRatingCtl = giveRatingController()

                successReview = giveReviewCtl.giveReview(new_review, agent_profile, current_user, current_role)

                successRating = giveRatingCtl.giveRating(new_rating, current_user, agent_profile, current_role, new_review)

                if((successRating == True) and (successReview == True)):
                    flash("Successfully reviewed", "success")
                    return redirect(url_for('web_app.my_reviews_index'))
                    #return redirect("/")
                    #return redirect(url_for("my_reviews_index"))
                    #return redirect("/my-reviews/")
                else:
                    flash("Error", "error")
                    return redirect("my_reviews_create")

            return render_template("pages/my-reviews/create.html", profile=session['username'])
        return redirect("/")
