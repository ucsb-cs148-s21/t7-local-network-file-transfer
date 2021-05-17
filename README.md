# LOFT: LOcal File Transfer #
It's not the cloud. It's closer to you. It's your loft.

## Description ##
Our app allows users to transfer files wirelessly on a local network.

## Tech Stack ##
- Backend: Python/Flask
- Frontend: HTML/JS, Qt

## User Roles ##
- Those looking to send files from a computer to another device connected to the same router.
- Those looking to receive files to their computer from another device connected to the same router.

# Installation #

## Prerequisites ##
- Two devices connected to the same router.
- One of the two devices must be a computer running Linux, Windows, or Mac to serve as the "Host".
- The "Host" computer must have port 2402 open.
### "Host" computer software requirements
- python3. To install python, follow the instructions here. https://www.python.org/downloads/
- git
- (Windows only) Build Tools for Visual Studio https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019
  - When installing, select the C++ Build Tools to install

## Dependencies ##
- PyQt5: Desktop Interface.
- Flask: Web Framework and server for serving client UI.
- Netifaces: Getting user's local ip address.
- Pytest: Python Testing

## Installation Steps ##
Warning: Security is not yet implemented. Anybody on the same network can access the webpage without any authentication. \
**Do not leave Loft running while not in use.**

### Linux ###
1. Install the Prerequisite's Software Requirements
2. Clone the directory
```
git clone https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git
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
python3 -m loft
```


### Windows ###
1. Install the Prerequisite's Software Requirements
2. Clone the directory
```
git clone https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git
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
git clone https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git
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
python3 -m loft
```

## Functionality (Full Instructions) ##
Warning: Security is not yet implemented. Anybody on the same network can access the webpage without any authentication. \
**Do not leave Loft running while not in use.**

The Host is the machine that runs the Loft application. The Client is the other device that will send or receive files.

#### First, enter a virtual environment.
Instructions for creating one are provided in the installation steps above.\
Linux/Mac:
```
. venv/bin/activate
```
Windows:
```
.venv\Scripts\Activate
```

### To send a file from the Host computer to the other device (Client): ###
1. Run Loft.
2. On the Host, Click on the `Send Files...` Button and select the file to send. (Close and restart if greyed)
3. Click on the `Start Connection` Button.
4. On the Client device's browser, open the shown address.
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
2. There's no security

## Testing ##
1. Run `pytest` from the application directory.

## Contributing ##

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request :D


### Members ###
- Andrew Tran (`at527`)
- Ethan Wu (`ethwu`)
- Douglas Yuan (`dougyuan`)
- Zackery Mondin (`zmondin`)
- Kevin Pham (`kevbbn`)
