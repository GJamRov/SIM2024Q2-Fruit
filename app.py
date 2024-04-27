from flask import Flask, Blueprint, render_template, request, redirect, session, flash
# Controller Imports
from controllers.login import LoginController

# Entity Imports
from entity.admin import SystemAdmin
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

class WebApp:

    def __init__(self, port, db):
        self.app = Flask(__name__)
        self.port = port
        self.app.secret_key = 'super secret key'  # for sessions
        self.blueprint = Blueprint('web_app', __name__)
        self.database = db

    def set_port(self, port: int):
        self.port = port

    def run_app(self):
        """Runs the web application."""
        self.blueprint.add_url_rule('/', 'home', self.home)
        self.blueprint.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout', 'logout', self.logout, methods=['POST'])
        self.blueprint.add_url_rule('/profile/<username>/', 'user_profile', self.user_profile)
        self.app.register_blueprint(self.blueprint)
        self.app.run(debug=True, port=self.port)

    def home(self):
        """View function for the index route."""
        # print(session)
        return render_template("index.html")
    
    ## User Functionalities
    def login(self):
        """User login route"""
        if request.method == 'POST':
            entered_username = request.form['username']
            entered_password = request.form['password']
            
            # Login Controller handles login
            loginCtl = LoginController(self.database)
            if loginCtl.validateLogin(entered_username, entered_password):
                session['username'] = entered_username
                flash('Login successful!', 'success')
                return redirect('/profile/' + entered_username)
            else:
                flash('Invalid username or password', 'error')
                
        return render_template('login.html')

    def logout(self):
        """User logout route"""
        if 'username' in session:
            username = session['username']
            user_found = next((user for user in self.users if user.username == username), None)
            if user_found:
                session.pop('username')
                flash('Logged out successfully', 'success')
            else:
                flash('User not found', 'error')
        else:
            flash('You are not logged in', 'error')
        return redirect('/')

    def user_profile(self, username=None):
        """View user profile"""
        if 'username' in session and username == session['username']:
            user_found = next((user for user in self.users if user.username == username), None)
            if user_found:
                role = type(user_found)
                if role == SystemAdmin:
                    return render_template("profile_admin.html", user=user_found)
                else:
                    flash('Invalid user role', 'error')
                    return redirect('/')
            else:
                flash('User not found', 'error')
                return redirect('/')
        flash('Unauthorized access! Please log in.', 'error')
        return redirect('/login')
    
    ## System Admin Functionalities
    #TODO: 3. Create user accounts
    def create_account(self):
        """Create new user account"""
        # Check that the user is a System Admin

        # Get form data from POST request

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

