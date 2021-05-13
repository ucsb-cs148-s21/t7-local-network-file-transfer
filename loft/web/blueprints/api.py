'''
The Loft API
============

Available Operations
--------------------

``POST``
  Send a file to the host. Send files through ``enctype="multipart/form-data"``.
``GET``
  Receive a file from the host. The parameter ``id`` specifies which file to
  receive. The contents of the file are sent as the body of the response.
``LIST``
  List a mapping of file ids to available file names. The listing is on the
  ``available`` field of the response object.
'''
import os
from pathlib import Path

from flask import abort, Blueprint, current_app, flash, jsonify, request, send_from_directory

from loft.util.file import save
from loft.util.id_map import IdMap


def api(available: IdMap):
    '''Handles upload and download requests.'''
    api = Blueprint('api', __name__)

    @api.route('/api', methods=['POST'])
    def receive():
        '''Receive a file via a POST request.'''

        if not request.files:
            flash('No file was selected.', 'error')
            # 400 Bad Request
            abort(400, description='No files were sent.')

        for _, f in request.files.items(multi=True):
            save(f, current_app.config['DOWNLOADS_FOLDER'])

        return jsonify(), 200

    @api.route('/api', methods=['GET'])
    def send():
        '''Send a requested file in response to a GET request.'''
        if 'id' not in request.args:
            abort(400, description='No file ID specified.')
        try:
            file_id = int(request.args['id'])
        except ValueError:
            abort(400, description='Bad file ID `{}`.'.format(
                request.args['id']))

        if not available.contains(file_id):
            abort(404, description='Invalid file ID {}.'.format(file_id))

        file_path: Path = available.get(file_id)
        assert file_path
        dirname: Path = file_path.parent
        basename: Path = file_path.name

        try:
            return send_from_directory(dirname, basename, as_attachment=True, cache_timeout=0), 200
        except FileNotFoundError:
            abort(404, description='File ID {} not available.'.format(file_id))

    @api.route('/api', methods=['LIST'])
    def inspect():
        '''Inspect what files are currently available.'''
        return jsonify(available={k: v.name for k, v in available.items()})

    return api
