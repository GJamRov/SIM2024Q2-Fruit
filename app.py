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
        self.blueprint.add_url_rule('/profile/<username>/', 'user_profile', self.user_profile)
        self.app.register_blueprint(self.blueprint)
        self.app.run(debug=True, port=self.port)

    def home(self):
        """View function for the index route."""
        return render_template("index.html")

    def user_profile(self, username=None):
        """View user profile"""
        if username is None:
            username = "User"
        return render_template("profile.html", username=username)