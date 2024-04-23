from flask import Flask, Blueprint, render_template, request, redirect, session, flash
from admin import SystemAdmin

class WebApp:

    def __init__(self, port, users):
        self.app = Flask(__name__)
        self.port = port
        self.app.secret_key = 'super secret key'  # for sessions
        self.blueprint = Blueprint('web_app', __name__)
        self.users = users  # List of objects

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

    def login(self):
        """User login route"""
        if request.method == 'POST':
            entered_username = request.form['username']
            entered_password = request.form['password']
            
            # Search for user by username
            user_found = next((user for user in self.users if user.username == entered_username), None)
            if user_found and user_found.login(entered_password):
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

    def home(self):
        """View function for the index route."""
        # session['_flashes'] = []
        print(session)
        return render_template("index.html")

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
