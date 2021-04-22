import sys
import webbrowser
import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from gevent.pywsgi import WSGIServer
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware

UPLOAD_FOLDER = 'uploads'
APP_NAME = 'loft'
HOST = '0.0.0.0'
PORT = 2402

gui = QApplication(sys.argv)
app = Flask(APP_NAME)
server = WSGIServer((HOST, PORT), app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def start_server(app, window):
    '''Start the web server and close the GUI window.'''
    def callback():
        if not(os.path.exists(UPLOAD_FOLDER)):
            os.mkdir(UPLOAD_FOLDER)
        window.close()
        webbrowser.open('http://localhost:{}'.format(PORT))
        # server.run(host=HOST, port=PORT)
        server.serve_forever()
    return callback


def main():
    window = QWidget()
    window.setWindowTitle('loft')
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)

    hello = QLabel('<i>hello</i>, world')

    button = QPushButton(text='start server', parent=window)
    button.clicked.connect(start_server(app, window))

    layout = QGridLayout(window)
    layout.addWidget(hello, 0, 0)
    layout.addWidget(button, 1, 0)

    window.show()
    sys.exit(gui.exec_())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quit')
def quit_server():
    # request.environ.get('werkzeug.server.shutdown')()
    server.stop()
    return 'good-bye'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    main()