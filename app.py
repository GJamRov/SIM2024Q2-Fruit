from flask import Flask, Blueprint, render_template, request, redirect, session, flash, url_for
# Controller Imports
from controllers.login import LoginController
from controllers.addAccount import addAccountCtl
from controllers.createProfile import createUserProfileController
from controllers.viewProfile import viewUserProfileController
from controllers.updateProfile import updateUserProfileController
from controllers.suspendProfile import suspendUserProfileController
from controllers.searchProfile import searchUserProfileController

# Entity Import
from entity.user import User

class WebApp:

    def __init__(self, port):
        self.app = Flask(__name__)
        self.port = port
        self.app.secret_key = 'super secret key'  # for sessions
        self.blueprint = Blueprint('web_app', __name__)

    def set_port(self, port: int):
        self.port = port

    def run_app(self):
        """Runs the web application."""
        self.blueprint.add_url_rule('/', 'home', self.home)
        self.blueprint.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout', 'logout', self.logout, methods=['GET', 'POST'])
        # self.blueprint.add_url_rule('/profile/<username>', 'profile', self.profile, methods=['GET', 'POST'])

        # user
        self.blueprint.add_url_rule('/users/', 'users_index', self.users_index, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/create', 'user_create', self.user_create, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/view', 'user_view', self.user_view, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/users/update', 'user_update', self.user_update, methods=['GET', 'POST'])
        # user profile
        self.blueprint.add_url_rule('/user-profiles/', 'user_profiles_index', self.user_profiles_index, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/create', 'user_profile_create', self.user_profile_create, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/view', 'user_profile_view', self.user_profile_view, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/user-profiles/update', 'user_profile_update', self.user_profile_update, methods=['GET', 'POST'])
        # property listing
        self.blueprint.add_url_rule('/property-listings/', 'property_listings_index', self.property_listings_index)

        self.app.register_blueprint(self.blueprint)
        User.connect_database("SampleDatabase")
        self.app.run(debug=True, port=self.port)

    def home(self):
        """View function for the index route."""
        # print(session)
        return render_template("pages/home.html")
    
    ## User Functionalities
    def login(self):
        """User login route"""
        template = 'login.html'
        
        #Request data from web page
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
        
        return render_template(template)         

    def logout(self):
        """User logout route"""

        #Clear session data and redirect to login page once logged out
        session.pop('username')
        session.pop('role')
        session.pop('logged_in', None)
        session['_flashes'].clear()
        #flash('Logout successful!', 'success')
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
                entered_confirm_password = request.form['confirm_password']
                entered_email = request.form['email']
                entered_profile = request.form['profile']

                if entered_password == entered_confirm_password:
                    # Send details to controller
                    addAccCtl = addAccountCtl()
                    acc_details = [entered_username, entered_password, entered_email, entered_profile]
                    addAccCtl.addUserAccount(session.get('username'), acc_details)

                else:
                    flash("Passwords don't match!", "error")

    #4. View user accounts
    def view_account(self):
        """View user accounts"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                pass

    #5. Update user accounts
    def update_account(self):
        """Update existing user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                pass

    #6. Suspend user account
    def suspend_account(self):
        """Suspend a user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                pass

    #7. Search user account
    def search_account(self):
        """Search user account"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                pass

    #TODO: 8. Create user profiles
    def create_profile(self):
        """Create new user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                UP = [request.form['profile_type'], request.form['profile_desc']]

                createProfileCtl = createUserProfileController()
                if createProfileCtl(UP):
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
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                entered_desc = request.form['profile_desc']

                updateProfileCtl = updateUserProfileController()
                if updateProfileCtl.updateUserProfile(profile, entered_desc):
                    flash("Profile description updated successfully!", "success")
                    return redirect('/user-profiles/')
                else:
                    flash("Failed to update profile. Please try again.", "error")
                    return redirect('/user-profiles/update')
            return render_template('pages/user-profiles/update.html', profile=profile)

    #TODO: 11. Suspend user profile
    def suspend_profile(self, profile):
        """Suspend user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            suspendUserProfileCtl = suspendUserProfileController()
            if suspendUserProfileCtl.suspendUserProfile(profile):
                flash("User profile suspended!", "success")
            else:
                flash("Error suspending user profile", "error")
            return redirect('/user-profiles/')


    #TODO: 12. Search user profile
    def search_profile(self):
        """Search user profile"""
        # Check that the user is a System Admin
        while session['role'] == 1:
            # Get form data from POST request
            if request.method == 'POST':
                entered_username = request.form['query-details']

                searchUserProfileCtl = searchUserProfileController()
                profile_data = searchUserProfileCtl.searchUserProfile(entered_username)
                
                if profile_data:
                    return render_template("pages/users/index.html", profiles=profile_data)
            return redirect('/user-profiles/')

    # user
    def users_index(self):
        """users index page"""
        return render_template("pages/users/index.html")

    def user_create(self):
        """create a user"""
        return render_template("pages/users/create.html")

    def user_view(self):
        """view a user"""
        return render_template("pages/users/view.html")

    def user_update(self):
        """update a user"""
        return render_template("pages/users/update.html")

    # user profile
    def user_profiles_index(self):
        """user profile index page"""
        return render_template("pages/user-profiles/index.html")

    def user_profile_create(self):
        """create a user profile"""
        return render_template("pages/user-profiles/create.html")

    def user_profile_view(self):
        """view a user profile"""
        return render_template("pages/user-profiles/view.html")

    def user_profile_update(self):
        """update a user profile"""
        return render_template("pages/user-profiles/update.html")

    # property listing
    def property_listings_index(self):
        """property listing index page"""
        return render_template("pages/property-listings/index.html")
