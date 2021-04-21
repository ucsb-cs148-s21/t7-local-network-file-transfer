
from flask import abort, Blueprint, Flask, render_template
from jinja2 import TemplateNotFound

landing = Blueprint('landing', __name__)


@landing.route('/')
def index():
    return render_template('pages/index.html')
