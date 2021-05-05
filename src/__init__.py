
import os

APP_NAME: str = 'loft'
HOST: str = '0.0.0.0'
PORT: int = 2402

# folder where we search for files to send
DOCUMENTS_FOLDER: str = '~{}Documents'.format(
    os.sep) if os.name == 'nt' else '~'

# folder where files uploaded on the web client are downloaded to
DOWNLOADS_FOLDER: str = '~{}Downloads'.format(os.sep)
