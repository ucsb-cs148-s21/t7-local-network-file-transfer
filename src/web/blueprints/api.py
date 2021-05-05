
import os

from flask import abort, Blueprint, current_app, flash, Flask, jsonify, \
    redirect, render_template, Request, request, send_from_directory
from jinja2 import TemplateNotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect

from ..inventory import Inventory
from util.file import save


def api(available: Inventory):
    '''Handles upload and download requests.'''
    api = Blueprint('api', __name__)

    @api.route('/api', methods=['POST'])
    def receive():
        '''Receive a file via a POST request.'''
        assert request.method == 'POST'

        if not request.files:
            flash('No file was selected.', 'error')
            # 400 Bad Request
            abort(400, description='No files were sent.')

        for file_input in request.files:
            for f in file_input:
                save(f, current_app.config['downloads_folder'])

        # 200 OK
        return redirect('landing.index'), 200

    @api.route('/api', methods=['GET'])
    def send():
        '''Send a file via a GET request.'''
        args = request.args
        if 'id' in args and available.contains(int(args['id'])):
            file_path = available.get(int(args['id']))
            assert file_path
            dirname = os.path.dirname(file_path)
            basename = os.path.basename(file_path)

            try:
                return send_from_directory(dirname, basename, as_attachment=True), 200
            except FileNotFoundError:
                abort(
                    404, description='File ID {} not available for download.'.format(args['id']))
        else:
            abort(400, description='File ID not provided or invalid.')

    @api.route('/api')
    def unimplemented():
        '''Catch-all for unimplemented requests.'''
        # 501 Not Implemented
        return {}, 501, {'ContentType': 'application/json'}

    return api
