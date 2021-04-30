
import os

from flask import abort, Blueprint, current_app, flash, Flask, \
    redirect, render_template, request, send_from_directory, url_for
from jinja2 import TemplateNotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect

from util.file import save

def create_blueprint(send_file_name_address):
    landing = Blueprint('landing', __name__)

    @landing.route('/')
    def index():
        return render_template('pages/index.html')


    @landing.route('/', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'upload' not in request.files:
                # POST request received, but no file attached
                return redirect(url_for('landing.index'))
            file = request.files['upload']
            # if user does not select file, browser also
            # submit an empty part without filename
            if not file:
                flash('No file was selected.', 'error')
                return redirect(url_for('landing.index'))

            save(file, current_app.config['downloads_folder'])

        return render_template('pages/index.html')

    @landing.route('/download/')
    def download():
        """Download a file."""
        print(send_file_name_address)
        file_name = send_file_name_address[0]
        file_path = send_file_name_address[1]

        try:
            return send_from_directory(file_path, file_name, as_attachment=True)
        except FileNotFoundError:
            abort(404)
    
    return landing

