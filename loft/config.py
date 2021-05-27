
from pathlib import Path
import shutil

from loft.util.file import get_downloads, get_documents


class Config:
    '''
    Configuration for the application.

    Any values that need to be exposed through Flask MUST be in `UPPERCASE`.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DOWNLOADS_FOLDER.mkdir(parents=True, exist_ok=True)
        self.DOCUMENTS_FOLDER.mkdir(parents=True, exist_ok=True)

    # Flask Configuration

    HOST: str = '0.0.0.0'
    PORT: int = 2402

    SECRET_KEY: str = 'bf7fe7847aa5f10778de0340d4b7cb5163d2727f95801ba0'

    # Loft Configuration
    APP_NAME: str = 'loft'

    # Folder where files uploaded on the web client are downloaded to.
    DOWNLOADS_FOLDER: Path = get_downloads()

    # Folder where we search for files to send.
    DOCUMENTS_FOLDER: Path = get_documents()

    # Loft Environment Variables

    # location of user config file
    config_filepath: str = 'LOFT_CONFIG'
    # whether or not to use HTTPS
    https: bool = False


class DebugConfig(Config):
    '''Configuration for testing.'''
    TESTING: bool = True

    DOWNLOADS_FOLDER: Path = Path('test', 'artifacts.tmp', 'downloads').resolve()
    DOCUMENTS_FOLDER: Path = Path('test', 'artifacts.tmp', 'documents').resolve()

    def __del__(self):
        shutil.rmtree(self.DOWNLOADS_FOLDER, ignore_errors=True)
        shutil.rmtree(self.DOCUMENTS_FOLDER, ignore_errors=True)


class LocalConfig(Config):
    '''Configuration for local serving only.'''
    HOST: str = 'localhost'
