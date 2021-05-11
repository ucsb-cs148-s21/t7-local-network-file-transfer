
import os
import subprocess
import sys
import typing

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


# The home directory, for convenience.
HOME: str = os.path.expanduser('~')


def home_slash(path: typing.List[str]) -> str:
    '''Formats a group of paths underneath the home directory.'''
    out = HOME
    if path:
        out += os.sep + os.sep.join(path)

    return out


def dup_name(name: str, duplicates: int) -> str:
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

    name, ext = os.path.splitext(name)
    return secure_filename('{}_{}{}'.format(name, duplicates, ext))


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
