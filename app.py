from flask import Flask, Blueprint, render_template, request, redirect, session, flash, url_for
# Controller Imports
from controllers.login import LoginController
from controllers.logout import LogoutController

# Entity Imports
from entity.admin import SystemAdmin
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

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
        self.blueprint.add_url_rule('/profile/<username>', 'profile', self.profile, methods=['GET', 'POST'])
        self.app.register_blueprint(self.blueprint)
        self.app.run(debug=True, port=self.port)

    def home(self):
        """View function for the index route."""
        # print(session)
        return render_template("index.html")
    
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
            print(role)
            #Session data assignment and page redirect on successful login
            if 0 < role < 5:
                session['username'] = entered_username
                session['role'] = role
                session['logged_in'] = True
                flash('Login successful!', 'success')
                return redirect(url_for('web_app.profile', username=session['username']))
            elif role == 5:
                flash('Account is suspended', 'error')
            elif role == 6:
                flash('Invalid username or password', 'error')            
        
        return render_template(template)         

    def logout(self):
        """User logout route"""
        username = session['username']

        # Logout Controller handles logout
        logoutCtl = LogoutController()
        if logoutCtl.logout(username):
            #Clear session data and redirect to login page once logged out
            session.pop('username')
            session.pop('role')
            session.pop('logged_in', None)
            flash('Logout successful!', 'success')
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
    #TODO: 3. Create user accounts
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

                #userAccount = (request.form['username'], request.form['password'], request.form['confirm_password'], request.form['email'], request.form['profile'])
        # SystemAdmin Object creates new user object based on form data

    #TODO: 4. View user accounts
    def view_account(self):
        pass

    #TODO: 5. Update user accounts
    def update_account(self):
        pass

    #TODO: 6. Suspend user account
    def suspend_account(self):
        pass

    #TODO: 8. Create user profiles
    def create_profile(self):
        pass

    #TODO: 9. View user profiles
    def view_profile(self):
        pass

    #TODO: 11. Suspend user profile
    def suspend_profile(self):
        pass

    #TODO: 12. Search user profile
    def search_profile(self):
        pass

