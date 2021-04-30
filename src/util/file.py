
import os
import subprocess
import sys

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def dup_name(name: str, i: int):
    '''Add duplicate tag to name if necessary.'''
    if i <= 0:
        return name

    name, ext = os.path.splitext(name)
    return secure_filename('{}_{}{}'.format(name, i, ext))


def save(file: FileStorage, dest: str):
    '''Save a file, renaming if duplicates are found.'''
    duplicates = 0

    destpath = os.path.join(dest, dup_name(
        file.filename or 'Untitled', duplicates))
    while os.path.exists(destpath):
        duplicates += 1
        destpath = os.path.join(dest, dup_name(
            file.filename or 'Untitled', duplicates))

    file.save(destpath)


def open_(path: str):
    '''Open the given path using the appropriate native application.'''
    if sys.platform == 'win32':
        os.startfile(path)
    else:
        subprocess.call(('open' if sys.platform ==
                        'darwin' else 'xdg-open', path))
