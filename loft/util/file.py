
import os
import subprocess
import sys
import typing
from pathlib import Path

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from PyQt5.QtCore import QStandardPaths


def get_downloads() -> Path:
    '''Returns a path to the system downloads folder.'''
    return Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation))


def get_documents() -> Path:
    '''Returns a path to the system documents folder.'''
    return Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation))


def get_data() -> Path:
    '''Returns a path to the application data folder.'''
    path = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation), 'Loft')
    path.resolve().mkdir(parents=True, exist_ok=True)
    return path


def split_filename(path: str) -> typing.Tuple[str, str]:
    '''Returns the filename and extensions of a path.'''
    path = Path(path)
    filename = path.stem
    extensions = ''.join(path.suffixes)

    for suf in path.suffixes:
        filename = filename.rsplit(suf)[0]

    return filename, extensions


def dup_name(name: str, duplicates: int):
    """Add duplicate tag to name if necessary.

    Args:
        name (str): [file name]
        duplicates (int): [number of duplicates]

    Returns:
        [string]: [the file name with an appended '_x' tag
                    if there is a duplicate]
    """
    if duplicates <= 0:
        return name

    name, ext = split_filename(name)
    return '{}_{}{}'.format(name, duplicates, ext)


def save(file: FileStorage, dest: Path):
    '''Save a file, renaming if duplicates are found.'''
    duplicates = 0

    destpath: Path = dest / \
        secure_filename(dup_name(file.filename or 'Untitled', duplicates))
    while os.path.exists(destpath):
        duplicates += 1
        destpath: Path = dest / \
            secure_filename(dup_name(file.filename or 'Untitled', duplicates))

    file.save(destpath)


def open_(path: Path):
    '''Open the given path using the appropriate native application.'''
    if sys.platform == 'win32':
        os.startfile(path)
    else:
        subprocess.call(('open' if sys.platform ==
                        'darwin' else 'xdg-open', path))
