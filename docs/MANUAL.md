# User Manual :heart: #

## Table of Contents ##
- [Product Description](#product-description-)
- [Product Purpose](#product-purpose-)
- [Intended Audience](#intended-audience-)
- [Using Loft](#using-loft-)
    - [Host or Client?](#knowing-your-role)
    - [Using the Native UI](#using-the-native-ui)
    - [Using the Web UI](#using-the-web-ui)
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
The method is wireless, but does not involve using an intermediate cloud storage platform (Google Drive, 
Dropbox, etc) or the cloud at all.

## Intended Audience 👨‍👩‍👧‍👦 ##

The motivation behind creating Loft was to satisfy a typical need that a college student may have: 
transferring homework assignments.

>Andrew needs to transfer a homework file he has scanned or annotated on their mobile device to his 
>computer in order to submit it. Unfortunately he does not have a USB cable, AirDrop compatibility, or 
>a fast internet connection. Loft is an ideal solution.

But beyond students, anyone who just needs a simple solution to move files between devices on the same network 
is also a member of Loft's intended audience.

## Using Loft 🧠 ##


### Knowing Your Role ###
There are two possible roles fulfilled by a Loft user: Host and Client. The <i>Host</i> is the laptop/desktop that 
installed and initializes Loft, and can send stuff to (and receive stuff from) the Client. The <i>Client</i>, mobile or computer, is 
the other device that can send to (and receive from) the Host. **Before going any further**, make sure the Host and Client are 
on the same local connection.

⚠️ The host-client denomination can be confusing to grasp. In terms of file transfer functionality, both devices can freely send 
& receive files! The host is not necessarily "hosting" a file that the client wants to receive. It is hosting the tools and processes 
by which Loft functions, which is why the app must be initialized from the host machine.

Depending on your role, you will interact with a different side of Loft, both of which are described just below.

### Using the Native UI ###
You are the Host. You will interact with Loft's remote control, the native UI, which appears upon initializing the app:

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/7bPd20E4SzO7MGriFmot_Screen%20Shot%202021-05-27%20at%2011.46.48%20PM.png" height="400px" width="270px" /> 


The main visual component of the native UI is the QR code. Whatever

#### Sending Files From the Native UI ####
Select `Start Connection` to begin sending and receiving files. Use the `Select Files…` button to select files to send. When finished, 
use the `Done Transferring` button to close Loft.

#### Receiving Files to the Native UI ####
Files received from the Client can be seen by selecting the `Open Downloads` button. **Do not leave Loft running while not in use.**



### Using the Web UI ###
You are the Client. You interact with Loft's web UI. After the Host has started Loft's connection, it appears at the QR code/link displayed 
on the Native UI:

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/64K085t6QueD9Ha4rvOY_Screen%20Shot%202021-05-27%20at%207.16.43%20PM.png" height="320px" width="469px" /> 

#### Sending Files From the Web UI ####
You can send files by first selecting files with the `Select Files…` button, and then selecting the `Send Selected Files` button. 

#### Receiving Files to the Web UI ####
Files sent from the Native UI can be downloaded by pressing the `Receive Files` button.


## Known Issues 🚧 ##
1. The Web UI remains open after Loft has been closed.
2. Using HTTPS gives an untrusted certificate warning on the client side.

## Testing 🔬 ##
Loft is tested using `pytest`. Test Loft by running `make test` in the repository root.
