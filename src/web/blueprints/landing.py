
import os

from flask import abort, Blueprint, current_app, flash, Flask, \
    render_template, request, send_from_directory
from jinja2 import TemplateNotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect

from util.file import save

landing = Blueprint('landing', __name__)


@landing.route('/')
def index():
    return render_template('pages/index.html')


@landing.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'upload' not in request.files:
            flash('No file part')
            redirect(request.url)
            return
        file = request.files['upload']
        # if user does not select file, browser also
        # submit an empty part without filename
        if not file:
            flash('No selected file')
            redirect(request.url)
            return

        save(file, current_app.config['downloads_folder'])

    return render_template('pages/index.html')
