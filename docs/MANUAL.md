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

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/OxCU5x7Ria9lkZGkL5Tc_Screen%20Shot%202021-06-07%20at%203.35.01%20PM.png" height="540px" width="280px" /> 

#### Connect ####
Let's look at the Security box. First, note the auto-generated username/password. Every time Loft is initialized, these credentials will change. The client must enter these credentials to access the Web UI.
Then, decide if you would like the Loft web UI to be situated at an HTTPS address for extra security. If so, select `Toggle HTTPS`. If not, 
leave it untouched. Then, in the Transfer box, select `Start Connection`. 

Now the main visual component of the native UI is the beautiful, giant QR code. On your client device, scan this QR code to discover the web UI. 
As a fallback (if the client cannot easily scan the QR), navigate directly to the blue URL underneath the code. A new QR code will be generated 
if HTTPS is toggled.

#### Sending Files From the Native UI ####
Use the `Send Files…` button to select files to send. For confirmation, the names of the selected files will display at the bottom of the 
UI, replacing the `No files selected` text. These files are immediately available to the client for download. Files can be reselected at 
any time by using `Send Files…` again, and this new set of files will be made available to the client. 

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/ZtcLlRIITAiapgHWn41L_Screen%20Shot%202021-05-28%20at%202.37.16%20AM.png" height="440px" width="290px" /> 
<sup>The Native GUI with HTTPS toggled and files selected.</sup>

#### Receiving Files to the Native UI ####
Files received from the Client can be seen by selecting the `Open Downloads` button. **Do not leave Loft running while not in use.**

#### Full Instructions ####
If there is any uncertainty about how to operate the native UI, clicking on the `Full Instructions` text at the bottom-left of the window 
will open a detailed instruction file in your web browser.
<br></br>

### Client: Using the Web UI ###
You are the Client. You interact with Loft's web UI. After the Host has started Loft's connection, scan the QR code or directly navigate to
the link displayed on the Native UI. You should see a login dialog; enter the username/password shown on the Native UI. The web UI should appear in your web browser now:

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/AEJRdzMDTOOnoXR5pWOP_Screen%20Shot%202021-05-28%20at%2011.15.41%20AM.png" height="310px" width="369px" /> 

#### Sending Files From the Web UI ####
You can send files by first selecting files with the `Select Files…` button. In the `Files Selected to Send` area, the file names will 
appear in individual bubbles for confirmation. These can be reselected at any time by using `Select Files…` again. Now, select the 
`Send Selected Files` button to perform the transfer. If the transfer is successful, a "Files Sent Successfully" message should appear 
above the module.

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/dN30AI96Q9KmFbolnDlw_Screen%20Shot%202021-05-28%20at%2011.34.38%20AM.png" height="285px" width="369px" /> 
<sup> The Web UI with files selected to send. </sup>

#### Receiving Files to the Web UI ####
Files sent from the Host will appear as individual bubbles in the `Files Available to Receive` area. If the Host updates the set of files 
they are sending, the `Files Available to Receive` will instantly update according to the changes. You don't have to accept all of these files. 
Select only the bubbles that contain the files you want; they will turn purple as confirmation. Now, select the `Receive Files` button to download them. 

<img src="https://s3.amazonaws.com/filepicker-images-rapgenius/vE90OmH6T46vQlY9fH9V_Screen%20Shot%202021-05-28%20at%2011.55.52%20AM.png" height="255px" width="369px" /> 
<sup> The Web UI with files available to receive. </sup> 

<sup> The client has selected two of these files to download, and has left one greyed out. </sup>
<br></br>
### Shutting Down Loft ###
You cannot shut down from the web UI. When you are done transferring files, select the `Done Transferring` button on the Native UI 
to shut down Loft. Remember to not leave Loft running while not in use!
<br></br>

## Known Issues 🚧 ##
1. The Web UI remains open after Loft has been closed.
2. Since we manually generate our own HTTPS certificates, using HTTPS raises an untrusted certificate warning on the client side.
You will need to disregard the warning and proceed to the web address.
3. The Windows executable excludes HTTPS support due to an incompatibility between the dependency and our packager. The functionality 
is still available if run from source.

## Testing 🔬 ##
Loft is tested using `pytest`. Test Loft by running `make test` in the repository root.

<br></br>
