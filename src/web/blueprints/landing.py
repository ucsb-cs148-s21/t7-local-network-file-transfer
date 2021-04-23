
import os

from flask import abort,  Blueprint, current_app, flash, Flask, render_template, request, send_from_directory
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware

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
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file.save(os.path.join(
            current_app.config['downloads_folder'], filename))
        return render_template('pages/index.html')
    return render_template('pages/index.html')
