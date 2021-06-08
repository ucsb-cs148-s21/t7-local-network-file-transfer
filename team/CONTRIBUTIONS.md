# Team 7 Local File Transfer Team Member Contributions

## Doug ##

My main contributions to the project were helping implement host uploads, mobile downloads, building the Loft binary executable
for Mac devices, and maintaining user manual and instruction documentation. 
- For host uploads, I worked on the native PyQt GUI, and collaborated with Andrew who worked on server-side components. 
- For mobile downloads, I collaborated extensively with Zack to coordinate back-end communication between host and client.
- Due to commit squashing/pair programming, a lot of work done regarding these two issues was not reflected in the contributions log.
- Building the Mac binary was an individual effort that encompassed a lot of challenges with Python packaging module `cx-Freeze`
  and compatibility challenges with other Mac devices.
- Writing the user manual, meeting notes, instructions, etc is pretty straightforward.

## Kevin Pham

### Code
- Worked on the upload feature to send files from one device to another
- Worked on the webpage UI, so users get feedback when files are uploaded, had some help from Ethan to  merge
- Implemented the QR code into the GUI for users to scan easily on their phone, had some help from Ethan to merge and implement.
- Worked on GUI to add instructions
- Did PR reviews

### Leadership
- Led a retro

### Miscellaneous
- Wrote a ton of meeting notes
- Worked on the MVP presentation by myself

## Zack ##
`The contributors section is highly innaccurate for my case because I was unfamiliar with Github and our tech stack for a lot of the quarter so my group took care of the commits while I learned from and worked with them.`
- Implemented the IP address function with Andrew so that our program could display the host's IP address to give a link for the user to follow
- Worked with Douglas to get the download functionality from host to client working, Douglas worked on the frontend while I worked on the backend
- Was in charge of packaging for Windows using pyinstaller while Andrew worked on packaging for Linux and Douglas worked on packaging for Mac
- Noticed an issue with our program being slow on windows so I worked to get it fixed, however, Ethan addded server threading in a future commmit which served as a fix for it.
- Setup the https toggle feature with Ethan.
- Before code freeze I worked to try and get the packaging working again for windows because the https feature broke it, however, Ethan and I were unable to fix it but Ethan was able to package with Windows by disabling https
- Overall I served as the tester for all new features making sure each aspect of our program worked

## Ethan ##
We’ve mostly been squash-and-merging PRs, so the total number of commits is relatively small 
compared to the total number of actual commits. Also, at least three PRs were merged directly 
into main by accident, which then contain the true number of intermediate commits from that
branch. Finally, we’ve been making changes to the documentation (_i.e._ user manual, meeting
notes, and the README) in commits directly to main, which also artificially inflates the
total number of commits.

I was responsible for the general architecture of the application, the design and implementation of
the web client UI, and the REST API exposed by the Flask server; as well as 
continuous integration testing of that API. I also wrote build scripts and led 
many of our meetings.

## Andrew ##

Summary: I was the product manager. I originated many of the user stories and wrote the acceptance criteria for the issues. My commit number looks inflated as I don't feel like I had the largest impact in terms of the code. I'm very happy with all of my team members and believe everybody made important contributions to the project.

- Proposed this project and was the product manager for Loft.
- Envisioned the design and user experience.
- Implemented a method of obtaining and displaying the server's IP Address.
- Managed the design of the native desktop QT interface.
- Implemented the first iteration of sending from Host to client from work started by Doug and Zack.
- Created the design diagram of the architecture.
- Fixed bug of old file being sent.
- Researched and created the initial Pyinstaller build command.
- Implemented HTTP Basic Authentication and updated the QT interface for it.
- Built the Appimages for Fedora, Debian, and Ubuntu released.
- Managed testing and building on Linux.
- My commit number looks little inflated. 
- I'm happy with all of my team members. 
- Everybody made important contributions.

