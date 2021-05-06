
from flask import Blueprint, render_template


<<<<<<< HEAD
def landing():
=======
from util.file import save


def create_blueprint(send_name_path):
>>>>>>> origin/main
    landing = Blueprint('landing', __name__)

    @landing.route('/')
    def index():
        return render_template('pages/index.html')

<<<<<<< HEAD
=======
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

            save(file, current_app.config['DOWNLOADS_FOLDER'])

        return render_template('pages/index.html')

    @landing.route('/download/')
    def download():
        """Download a file."""
        file_name = send_name_path['file_name']
        file_path = send_name_path['file_path']

        try:
            return send_from_directory(file_path, file_name, as_attachment=True, cache_timeout=0)
        except FileNotFoundError:
            abort(404)

>>>>>>> origin/main
    return landing
