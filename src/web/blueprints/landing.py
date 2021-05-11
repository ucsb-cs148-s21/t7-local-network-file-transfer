
from flask import Blueprint, render_template


def landing():
    landing = Blueprint('landing', __name__)

    @landing.route('/')
    def index():
        return render_template('pages/index.html')

    return landing
