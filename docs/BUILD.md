# Building Your Loft #
Do you want to build your own Loft? Get started here!

> Is building your own Loft too difficult? Then head over [here](https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/releases) to get a prefabricated Loft.

## Table of Contents ##
- [Dependencies](#gathering-the-materials)
- [Building](#putting-it-all-together)

## Gathering the Materials ##
Building your Loft can be challenging if you’ve never built one before, but it’s super rewarding to have a place to send your stuff! In order to build your Loft, you’ll need [Python 3.9](https://www.python.org). Install Python on your computer and download this repository. You can either download the repository as a `.zip` file or use [Git](https://git-scm.com).

## Putting it All Together ##

1. Either unzip the zipped repository or clone the repository with Git. You can put them anywhere, but we’ll assume you put them on your desktop (`~/Desktop` on Linux and macOS, `C:\Users\<username>\Desktop`). If you put the repository somewhere else, change the file paths as necessary. If using Git:
  ```shell
  $ # on Linux or macOS
  $ cd ~/Desktop
  $ git clone 'https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git'
  $ cd t7-local-network-file-transfer
  ```
  
  ```powershell
  > # in Windows PowerShell
  > Set-Location $home\Desktop
  > git clone 'https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer.git'
  > Set-Location t7-local-network-file-transfer
  ```
2. Set up and activate a Python virtual environment (recommended).
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
  $ python3 -m pip install -r requirements.txt
  ```
  
  ```powershell
  > py -3 -m pip install -r requirements.txt
  ```
4. Build your Loft!
  ```shell
  $ make build
  ```
  
  ```powershell
  > py -3 -OO -m build
  ```

Your new Loft will now be inside the `dist/` directory. Feel free to set it up somewhere convenient, like `~/Applications` on Mac! You can now delete the Loft repository.
```shell
$ cd ~/Desktop
$ rm -rf t7-local-network-file-transfer
```

```powershell
> Set-Location $home\Desktop
> Remove-Item t7-local-network-file-transfer -Recurse
```
