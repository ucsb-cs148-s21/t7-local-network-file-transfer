#! /usr/bin/env python3
'''
``build.py``
============

Build script for Loft.

Usage
-----

Linux & macOS
^^^^^^^^^^^^^
In ``bash`` or similar::

    $ python3 -m venv .venv     # optional
    $ source .venv/bin/activate # optional
    $ python3 -m pip install -r requirements.txt
    $ python3 -OO -m build

Windows
^^^^^^^
In PowerShell::

    PS > py -m venv .venv           # optional
    PS > .venv/Scripts/Activate.ps1 # optional
    PS > py -m pip install -r requirements.txt
    PS > py -OO -m build
'''
from pathlib import Path
import platform
import typing

import PyInstaller.__main__

# the name of the application
NAME: str = 'loft'
# the entry point of the application
ENTRY_POINT: Path = Path('loft', '__main__.py')
# directory containing Flask resources
FLASK_RESOURCES: Path = Path('loft', 'web')

# resources that need to be bundled with the application
RESOURCES: typing.List[Path] = [
    Path(FLASK_RESOURCES, 'templates'), Path(FLASK_RESOURCES, 'static')]


def main():
    pathsep: str = ';' if platform.system() == 'Windows' else ':'
    PyInstaller.__main__.run([
        str(ENTRY_POINT),
        '-n', str(NAME),
        '--onefile',
        '--noconsole',
    ] + [f(res) for res in RESOURCES for f in (lambda _: '--add-data', lambda res: f'{res}{pathsep}{res}')])


if __name__ == '__main__':
    main()
