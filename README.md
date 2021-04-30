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
Loft requires `pyqt5` and `flask`.

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


## Installation ##


## Prerequisites ##
- Two devices connected to the same router.
- One of the two devices must be a computer running Linux, Windows, or Mac to serve as the "host".
- The "host" computer must have port 2402 open.
### "host" computer software requirements
- python3. To install python, follow the instructions here. https://www.python.org/downloads/
- virtualenv. Install after installing python. https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
- git
- (Windows only) Build Tools for Visual Studio https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019
  - When installing, select the C++ Build Tools to install

## Dependencies ##
- netifaces

## Installation Steps ##
### Linux ###
1. Install the Prerequisite's Software Requirements
2. Clone the directory
```
git clone 
```
3. Create and start a python virtual environment
```
python3 -m venv venv
. venv/bin/activate
```
4. Install dependencies
```
python3 -m pip install -r requirements.txt
```

5. Run Loft
```
python3 src
```


### Windows ###
1. Install the Prerequisite's Software Requirements
2. Clone the directory
```
git clone 
```

3. Create and start a python virtual environment
```
py -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies
```
py -m pip install -r requirements.txt
```

5. Run Loft
```
py src
```


### Mac ###
1. Install the Prerequisite's Software Requirements
2. Clone the directory
```
git clone 
```
3. Create and start a python virtual environment
```
python3 -m venv venv
. venv/bin/activate
```
4. Install dependencies
```
python3 -m pip install -r requirements.txt
```

5. Run Loft
```
python3 src
```

## Functionality ##
The Host is the machine that runs the Loft application. The Client is the other device that will send or receive files.

### To send a file from the Host computer to the other device (Client):###
1. Run Loft.
2. Select the file to send.
3. Click on the `Start Connection` Button.
4. Open the shown address in the Client device's browser.
5. Select the `Receive File` button to download the file.
6. Back on the Host machine, select `Done Transferring`.

### To receive a file to the Host computer from the other device (Client): ###
1. Run Loft.
3. Click on the `Start Connection` Button.
4. Open the shown address in the Client device's browser.
5. Select `Select File...` and choose the file.
6. Select `Send Selected File` 
7. Back on the Host machine, select `Open Downloads` to view the directory containing the received file.
8. Select `Done Transfering`

## Known Problems ##
1. Selecting/Reselecting a file to send is not supported after the connection is started.

## Contributing ##
