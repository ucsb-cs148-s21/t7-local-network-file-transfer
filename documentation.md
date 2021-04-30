# LOFT: LOcal File Transfer #
It's not the cloud. It's closer to you. It's your loft.

## Description ##
Our app allows users to transfer files wirelessly on a local network.

## Prequisites ##
Users must already have python installed. To install python, follow the instructions here. https://www.python.org/downloads/

Windows users must also install VS Code with developer build tools. VS code and the developer build tools can be found here. https://code.visualstudio.com/download

### Dependencies ###
Loft requires `pyqt5` and `flask`.


### Downloading the Code ###
Visit the repo here. https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/
<img width="416" alt="Screen Shot 2021-04-29 at 8 07 05 PM" src="https://user-images.githubusercontent.com/46585109/116643689-7b744180-a926-11eb-95a2-9bcf4423dc8a.png">
Click the green "Code" button and download zip. After that extract the files. Next, open a terminal and navigate your way into the folder.


#### Setting Up a Virtual Environment ####
It is recommended that you set up a python virtual environment before installing
dependencies. You can set one up and activate it as follows:

First, follow the instructions here to install virtualenv. https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
Then, in the terminal follow these instructions

```
# on Linux and macOS
$ python3 -m venv env
$ source env/bin/activate
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

