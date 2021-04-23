# LOFT: LOcal File Transfer #
It's not the cloud. It's closer to you. It's your loft.

## Description ##
Our app allows users to transfer files wirelessly on a local network.

## Tech Stack ##
- Backend: Python/Flask
- Frontend: HTML/JS, Qt

## User Roles ##
- Those looking to send files to another user/device.
- Those looking to receive files from another user/device.

### Members ###
- Andrew Tran (`at527`)
- Ethan Wu (`ethwu`)
- Douglas Yuan (`dougyuan`)
- Zackery Mondin (`zmondin`)
- Kevin Pham (`kevbbn`)

## Running ##
Run the application with:
```
$ python src
```

### Dependencies ###
Loft requires `pyqt5`, `flask`, and `gevent`.

#### Setting Up a Virtual Environment ####
It is recommended that you set up a python virtual environment before installing
dependencies. You can set one up and activate it as follows:
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

### Dev-Dependencies ###
Format source with `autopep8`.
