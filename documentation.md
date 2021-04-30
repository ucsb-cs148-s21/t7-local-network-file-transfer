# LOFT: LOcal File Transfer #
It's not the cloud. It's closer to you. It's your loft.

## Description ##
Our app allows users to transfer files wirelessly on a local network.

## Prequisites ##
Users must already have python installed. To install python, follow the instructions here. https://www.python.org/downloads/
Windows users must also install VS Code with developer build tools. VS code can be found here. https://code.visualstudio.com/download

### Dependencies ###
Loft requires `pyqt5` and `flask`.

.<img width="1403" alt="Screen Shot 2021-04-28 at 10 59 52 PM" src="https://user-images.githubusercontent.com/46585109/116508086-730ffe00-a875-11eb-81b5-538db2590ee5.png">

#### Setting Up a Virtual Environment ####
It is recommended that you set up a python virtual environment before installing
dependencies. You can set one up and activate it as follows:

First, follow the instructions here to install virtualenv. https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
Then, in the terminal follow these instructions

```
# on Linux and macOS
$ python -m venv .venv
$ source .venv/bin/activate
# on Windows
$ py -m venv .venv
$ .venv/Scripts/activate
```

#### Installing Dependencies ####
Install dependencies:
```
# on Linux and macOS
$ python -m pip install -r requirements.txt
```

## Running ##
Run the application with:
```
$ python src
```

