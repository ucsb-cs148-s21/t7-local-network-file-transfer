
import os
import tempfile

from util.file import HOME, home_slash


class Config:
    '''
    Configuration for the application.

    Any values that need to be exposed through Flask MUST be in `UPPERCASE`.
    '''

    # Flask Configuration

    HOST: str = '0.0.0.0'
    PORT: int = 2402

    SECRET_KEY: str = 'bf7fe7847aa5f10778de0340d4b7cb5163d2727f95801ba0'

    # Loft Configuration
    APP_NAME: str = 'loft'

    # Folder where files uploaded on the web client are downloaded to.
    DOWNLOADS_FOLDER: str = home_slash(['Downloads'])

    # Folder where we search for files to send.
    DOCUMENTS_FOLDER: str = home_slash(
        ['Documents']) if os.name == 'nt' else HOME

    # Loft Environment Variables

    # location of user config file
    config_filepath: str = 'LOFT_CONFIG'


class TestingConfig(Config):
    '''Configuration for testing.'''
    TESTING: bool = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.downloads_ctx = tempfile.TemporaryDirectory()
        self.documents_ctx = tempfile.TemporaryDirectory()

    @property
    def DOWNLOADS_FOLDER(self) -> str:
        return self.downloads_ctx.name

    @property
    def DOCUMENTS_FOLDER(self) -> str:
        return self.documents_ctx.name

    def __del__(self):
        self.downloads_ctx.close()
        self.documents_ctx.close()
        del self.downloads_ctx
        del self.documents_ctx


class LocalConfig(Config):
    '''Configuration for local serving only.'''
    HOST: str = 'localhost'
