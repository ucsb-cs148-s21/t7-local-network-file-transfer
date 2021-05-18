
import sys

from cx_Freeze import setup, Executable

application_title = "Loft"
main_python_file = "loft/__main__.py"


base = None
if sys.platform == "win32":
    base = "Win32GUI"


buildOptions = dict(include_files=['loft/web/templates/', 'loft/web/static/'])

setup(
    name=application_title,
    version="0.1.0",
    description="An application to wirelessly transfer files between devices on the same local network.",
    options=dict(build_exe=buildOptions),
    executables=[
        Executable(main_python_file, base=base)
    ]
)
