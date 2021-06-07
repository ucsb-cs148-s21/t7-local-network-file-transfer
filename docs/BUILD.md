# Building Your Loft #
Do you want to build your own Loft? Get started here!

> Is building your own Loft too difficult? Then head over [here](https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/releases) to get a prefabricated Loft.

## Table of Contents ##
- [Dependencies](#gathering-the-materials)
- [Building](#putting-it-all-together)

## Gathering the Materials ##
Building your Loft can be challenging if you’ve never built one before, but it’s super rewarding to have a place to send your stuff! In order to build your Loft, you’ll need [Python 3.9](https://www.python.org). On Windows, you’ll also need the [C++ Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). Install Python on your computer and download this repository. You can either download the repository as a `.zip` file or use [Git](https://git-scm.com).

> By default, Loft uses port `2402` on your computer in order to connect. If that port is not available, set the key `PORT` in `loft/config.py` to an available port before building.

### The Nuts and Bolts ###
Loft depends on:
- `cryptography`
- `Flask`
- `Flask-HTTPAuth`
- `netifaces`
- `pyinstaller`
- `PyQt5`
- `qrcode`
- `Werkzeug`

#### Allen Wrenches ####
On macOS, you'll need `cx-Freeze` instead of `pyinstaller`.

### Hammers and Jackhammers ###
For development, your Loft will need:
- `autopep8`
- `pytest`

## Putting it All Together ##

1. Either unzip the zipped repository or clone the repository with Git. You can put them anywhere, but we’ll assume you put them on your desktop (`~/Desktop` on Linux and macOS, `C:\Users\<username>\Desktop` on Windows). If you put the repository somewhere else, change the file paths as necessary. If using Git:
    ```shell
    $ # on Linux or macOS
    $ cd ~/Desktop
    $ git clone 'https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git'
    $ cd t7-local-network-file-transfer
    ```

    ```powershell
    > # in Windows PowerShell
    > git clone 'https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git'
    > Set-Location t7-local-network-file-transfer
    ```
2. Set up and activate a Python virtual environment.
    ```shell
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    ```

    ```powershell
    > py -3 -m venv .venv
    > .venv\Scripts\Activate.ps1
    ```
3. Install dependencies.
    ```shell
    $ pip install -r requirements.txt
    ```

    ```powershell
    > pip install -r requirements.txt
    ```
4. Build your Loft!
    ```shell
    $ make build
    ```

    ```powershell
    > py -3 -OO -m build
    ```

On Windows and Linux, your new Loft will now be inside the `dist/` directory. For Mac, Loft will be located in `build/` instead. Feel free to set it up somewhere convenient, like `~/Applications` on Mac! You can now delete the Loft repository.
```shell
$ cd ~/Desktop
$ rm -rf t7-local-network-file-transfer
```

```powershell
> Set-Location $home\Desktop
> Remove-Item -Recurse 't7-local-network-file-transfer'
```
