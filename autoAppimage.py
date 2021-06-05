import subprocess
import sys

# Get Requirements
def get_requirements():
    subprocess.run(["python3", "-m", "pip", "install", "-r", "requirements.txt"])

# Build Pyinstaller image
def build_pyinstaller():
    subprocess.run(["make", "build"])

# Build Appimage
def build_appimage():
    subprocess.run(["./Appimage/linuxdeploy-x86_64.AppImage", 
                    "--appdir", "Appdir" , 
                    "-e", "dist/loft", 
                    "--output", "appimage", 
                    "--create-desktop-file" , 
                    "--icon-file" , "Appimage/loft.png"])

def main(pkg_manager):
    get_requirements()
    build_pyinstaller()
    build_appimage()

if __name__ == '__main__':
    main(sys.argv[0])
