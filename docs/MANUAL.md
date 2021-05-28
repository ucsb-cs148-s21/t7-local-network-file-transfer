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

## Intended Audience 👨‍👩‍👧‍👦 ##
The motivation behind creating Loft was to satisfy a typical need that a college student may have: 
transferring homework assignments.

>Andrew needs to transfer a homework file he has scanned or annotated on his mobile device to his 
>computer in order to submit it. Unfortunately he does not have a USB cable, AirDrop compatibility, or 
>a fast internet connection. Loft is an ideal solution.

But beyond students, anyone who just needs a simple solution to move files between devices on the same network 
is also a member of Loft's intended audience.

## Using Loft 🧠 ##

### Knowing Your Role ###
There are two possible roles fulfilled by a Loft user: Host and Client. The <i>Host</i> is the laptop/desktop that 
installed and initializes Loft; it can send stuff to (and receive stuff from) the Client. The <i>Client</i> is any other device,
but usually a phone or tablet; it can send to (and receive from) the Host. **Before going any further**, make sure the 
Host and Client are on the same local connection.

⚠️ The host-client denomination can be hard to grasp. In terms of file transfer functionality, both devices can freely send 
& receive files! The host is not necessarily "hosting" files that the client wants to receive; in fact it is often the 
other way around. Instead, it is hosting the tools and processes that are required for Loft to function. As such, the app must be 
started up (and shut down) from the host machine.

Depending on your role, you will interact with a different side of Loft, both of which are described just below.

### Host: Using the Native UI ###
You are the Host. Initialize Loft. You will interact with Loft's remote control, the native UI, which should appear on your screen now:

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/7bPd20E4SzO7MGriFmot_Screen%20Shot%202021-05-27%20at%2011.46.48%20PM.png" height="400px" width="270px" /> 

#### Connect ####
First, decide if you would like the Loft web UI to be situated at an HTTPS address for extra security. If so, select `Toggle HTTPS`. If not, 
leave it untouched. Then, select `Start Connection`. 

Now the main visual component of the native UI is the beautiful, giant QR code. On your client device, scan this QR code to bring up 
the web UI on the client's web browser. As a fallback (when the client cannot easily scan the QR), navigate directly to the 
blue URL underneath the code. A new QR code will be generated if HTTPS is toggled.

#### Sending Files From the Native UI ####
Use the `Send Files…` button to select files to send. For confirmation, the names of the selected files will display at the bottom of the 
UI, replacing the `No files selected` text. These files are immediately available to the client for download. Files can be reselected at 
any time by using `Select Files…` again, and this new set of files will be made available to the client. 

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/ZtcLlRIITAiapgHWn41L_Screen%20Shot%202021-05-28%20at%202.37.16%20AM.png" height="440px" width="290px" /> 
<sup>The Native GUI with HTTPS toggled and files selected. N.b. the QR code has changed.</sup>

#### Receiving Files to the Native UI ####
Files received from the Client can be seen by selecting the `Open Downloads` button. **Do not leave Loft running while not in use.**

#### Full Instructions ####
If there is any uncertainty about how to operate the native UI, clicking on the `Full Instructions` text at the bottom-left of the window 
will open a detailed instruction file in your web browser.
<br></br>

### Client: Using the Web UI ###
You are the Client. You interact with Loft's web UI. After the Host has started Loft's connection, scan the QR code or directly navigate to
the link displayed on the Native UI. The web UI should appear in your web browser now:

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/64K085t6QueD9Ha4rvOY_Screen%20Shot%202021-05-27%20at%207.16.43%20PM.png" height="320px" width="469px" /> 

#### Sending Files From the Web UI ####
You can send files by first selecting files with the `Select Files…` button. Underneath it, the file names will appear in individual bubbles 
for confirmation. Files can be reselected at any time by using `Select Files…` again. Then, select the `Send Selected Files` button.

#### Receiving Files to the Web UI ####
Files sent from the Native UI can be downloaded by selecting the `Receive Files` button.
<br></br>

### Shutting Down Loft ###
You cannot shut down from the web GUI. When you are done transferring files, select the `Done Transferring` button on the Native GUI 
to shut down Loft. Remember to not leave Loft running while not in use!
<br></br>

## Known Issues 🚧 ##
1. The Web UI remains open after Loft has been closed.
2. Since we manually generate our own HTTPS certificates, using HTTPS raises an untrusted certificate warning on the client side.
You will need to disregard the warning and proceed to the web address.

## Testing 🔬 ##
Loft is tested using `pytest`. Test Loft by running `make test` in the repository root.

<br></br>
