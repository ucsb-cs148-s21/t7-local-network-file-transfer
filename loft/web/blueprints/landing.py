
from flask import Blueprint, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from loft.config import Config 

def landing():
    landing = Blueprint('landing', __name__)

    auth = HTTPBasicAuth()

    users = {
        "loft": generate_password_hash(Config.DEFAULT_PASSWORD)
    }

    @auth.verify_password
    def verify_password(username, password):
        if username in users and \
            check_password_hash(users.get(username), password):
            return username

    @landing.route('/')
    @auth.login_required
    def index():
        return render_template('pages/index.html')

    return landing
