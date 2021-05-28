# User Manual #

## Table of Contents 📑 ##
- [Product Description](#product-description-)
- [Product Purpose](#product-purpose-)
- [Intended Audience](#intended-audience-)
- [Using Loft](#using-loft-)
    - [Host or Client?](#knowing-your-role)
    - [Using the Native UI](#host-using-the-native-ui)
    - [Using the Web UI](#client-using-the-web-ui)
    - [Shutting Down](#shutting-down-loft)
- [Known Issues](#known-issues-)
- [Testing](#testing-)

## Product Description 🏠 ##
>It’s not the cloud. It’s closer. It’s your Loft.

Loft is a local web application that quickly and easily transfers files between your devices, without using the Internet! 

Loft is built using a collection of Python libraries and frameworks (Flask, Werkzeug, PyQt); 
[here](https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/docs/BUILD.md) are the detailed instructions to 
build your own Loft! You can also find a prefabricated Loft [here](https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/releases) 🏚️.

## Product Purpose 🎯 ##
Loft's purpose is to provide multiple devices on the same local connection with a simple method to move files amongst each other. 
The method is wireless, but does not involve an intermediate cloud storage platform (Google Drive, Dropbox, etc) or the cloud at all.

## Sending and Receiving Files from the Native UI ##
Select `Start Connection` to begin sending and receiving files. Use the `Select Files…` button to select files to send. When finished, use the `Done Transferring` button to close Loft. Files received from the Web UI can be seen by selecting the `Open Downloads` button. If the `Select Files…` button is grayed out, you must restart Loft. **Do not leave Loft running while not in use.**

## Sending and Receiving Files from the Web UI ##
Follow the link displayed on the Native UI on your second device in order to access the Web UI. From the Web UI, you can send files by first selecting files with the `Select Files…` button, and then selecting the `Send Selected Files` button. Files sent from the Native UI can be downloaded by pressing the `Receive Files` button. The Web UI will no longer function once Loft has been closed from the Native UI.

## Known Issues ##
1. Selecting/Reselecting a file to send is not supported after the connection is started.
2. The Web UI remains open after Loft has been closed.
3. There's no security. Your Loft is a little rickety.

## Testing ##
Loft is tested using `pytest`. Test Loft by running `make test` in the repository root.
