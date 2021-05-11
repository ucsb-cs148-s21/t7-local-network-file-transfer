
import os
from os.path import split
import subprocess
import sys
import typing
from pathlib import Path

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


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


def save(file: FileStorage, dest: str):
    '''Save a file, renaming if duplicates are found.'''
    duplicates = 0

    destpath = os.path.join(dest, dup_name(
        file.filename or 'Untitled', duplicates))
    while os.path.exists(destpath):
        duplicates += 1
        destpath = os.path.join(dest, secure_filename(
            dup_name(file.filename or 'Untitled', duplicates)))

    file.save(destpath)


def open_(path: str):
    '''Open the given path using the appropriate native application.'''
    if sys.platform == 'win32':
        os.startfile(path)
    else:
        subprocess.call(('open' if sys.platform ==
                        'darwin' else 'xdg-open', path))
