#! /usr/bin/env python3
'''
``build.py``
============

Build script for Loft. Must be run from inside a venv named ``.venv``.

Usage
-----

Linux & macOS
^^^^^^^^^^^^^
In ``bash`` or similar::

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ python3 -OO -m build

Windows
^^^^^^^
In PowerShell::

    PS > py -m venv .venv
    PS > .venv/Scripts/Activate.ps1
    PS > pip install -r requirements.txt
    PS > py -3 -OO -m build
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

    args = [
        str(ENTRY_POINT),
        '-n', str(NAME),
        '--onefile',
        '--clean',
        '--noconsole',
        # '--hidden-import', 'cryptography',
        # '--hidden-import', 'cffi',
        # '--additional-hooks-dir', 'hooks',
        '--debug', 'all',
    ] + [f(res) for res in RESOURCES for f in (lambda _: '--add-data', lambda res: f'{res}{pathsep}{res}')]

    if platform.system() == 'Windows':
        venv = Path('.venv')
        if venv.is_dir():
            args += ['--paths', str(Path('.venv', 'Lib', 'site-packages'))]

    PyInstaller.__main__.run(args)


if __name__ == '__main__':
    main()
