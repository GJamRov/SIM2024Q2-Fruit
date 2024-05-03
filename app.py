from flask import Flask, Blueprint, render_template, request


class WebApp:

    def __init__(self, port):
        self.app = Flask(__name__)
        self.port = port
        self.blueprint = Blueprint('web_app', __name__)

    def set_port(self, port: int):
        self.port = port

    def run_app(self):
        """Runs the web application."""
        self.blueprint.add_url_rule('/', 'home', self.home)
        # self.blueprint.add_url_rule('/profile/<username>/', 'user_profile', self.user_profile)

        # user
        self.blueprint.add_url_rule('/users/', 'users_index', self.users_index)
        self.blueprint.add_url_rule('/users/create', 'user_create', self.user_create)
        self.blueprint.add_url_rule('/users/view', 'user_view', self.user_view)
        self.blueprint.add_url_rule('/users/update', 'user_update', self.user_update)
        # user profile
        self.blueprint.add_url_rule('/user-profiles/', 'user_profiles_index', self.user_profiles_index)
        self.blueprint.add_url_rule('/user-profiles/create', 'user_profile_create', self.user_profile_create)
        self.blueprint.add_url_rule('/user-profiles/view', 'user_profile_view', self.user_profile_view)
        self.blueprint.add_url_rule('/user-profiles/update', 'user_profile_update', self.user_profile_update)
        # property listing
        self.blueprint.add_url_rule('/property-listings/', 'property_listings_index', self.property_listings_index)

        self.app.register_blueprint(self.blueprint)
        self.app.run(debug=True, port=self.port)

    # example templates
    def home(self):
        """View function for the index route."""
        return render_template("pages/home.html")

    def user_profile(self, username=None):
        """View user profile"""
        if username is None:
            username = "User"
        return render_template("profile.html", username=username)

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
