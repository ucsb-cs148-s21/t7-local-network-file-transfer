# About me

Hi I'm Andrew! Currently I'm a 2nd year Computer Science Major. I haven't had much experience building entire programs, so hopefully this is the next step for me to actually do some "real" programming. I look forward to working and learning with everybody. In my spare time I enjoy photography and messing around with Linux.

# Norms

- We should be present for scheduled class and section times.
- We should be present when non-class time is scheduled and mutually agreed upon.
- We sould have goals set with deadlines to keep track of our progress.

# Project Ideas

The overall purpose of my local file transfer idea is to make it easier to transfer files wirelessly between machines without the ability/necessity of uploading to an external server. I have found several edge type cases with this.

1. User has no wireless capability - e.g. on airplane.
2. User can connect to a network and be discovered - e.g. at home or a network that allows discovery.
3. User cannot be discovered on network - e.g. UCSB wifi?

These cases lead to several ideas I have for file transfer. Maybe we can implement all of them.

## QR code / Animated QR Code

QR codes can be used to send small things like text between two machines. This just requires camera access and should be relatively easy to implement. For slightly larger files, we can animate the qr code so that the data becomes a sequence of codes. This is has a limited bandwidth though.

## Network Transfer

This is likely the fastest way to transfer files. There are several methods though. 

- https server (maybe the most universal?)
- sftp server
- samba server

They all requre a PC to act as a server for incoming and outgoing files which I think would be the easiest to implement. I have looked into using mobile devices as the host, but Apple is annoying and doesnt support the Wifi Direct standard.

It would also be useful to use QR codes in this method to facilitate connecting the machines.

Maybe we could use the PC to generate the wireless network itself? I haven't looked into what this is like for Windows and Mac.

## Network but with no discovery

All I can think of for this case is Bluetooth which can be slow and annoying. Alternatively we'd have to figure out how to directly connect two machines on a network like UCSB's eduroam with some sort of peer to peer connection that doesn't require traversing an external server. (web sockets?)
