
import os

from flask import abort, current_app, Blueprint, Flask, render_template, request, send_from_directory
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware

landing = Blueprint('landing', __name__)


@landing.route('/')
def index():
    return render_template('pages/index.html')


def allowed_file(filename):
    return True


@landing.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['downloads_folder'], filename))
            return render_template('pages/index.html')
    return render_template('pages/index.html')
