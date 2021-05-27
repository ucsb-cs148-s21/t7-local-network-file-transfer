# Lccal File Transfer #


Meeting Time: lab04

Type of Meeting: Stand-Up + Sprint Planning

Mentor: Vincent Tieu

Team: 
- [x] Ethan Wu
- [x] Douglas Yuan 
- [x] Zackery Mondin
- [x] Andrew Tran 
- [x] Kevin Pham

## Standup ##
- Ethan - Working on acccessibility, changing colors and adding labels. Has one outstanding PR.
- Zackery - Worked on downloads feature with douglas and got it working to the point where PyQT recognizes the file path and was able to get download working on flask. Right now it is hardcoded with a filepath from Zack's computer.
- Douglas - Worked on downloads with Zack. Same thing basically. Going to try to finish it today
- Kevin - Worked on the documentation file, waiting for further features to be added before continuing on the document. Will work forther on that file today.
- Andrew - Got PR's merged in. Looking to help the team finish the download feature


## Sprint Planning ##
For Sprint03, the team plans to:

- Implement unit testing for:
  - `landing.py`

- Implement QR Code for discovery

- Start thinking about security

- Work on Flask configuration

- Set up refactoring for proper REST API

- Do a wider refactor possibly involving:
  - New data structure
  - Use of external database
  - Config file

- Create an app favicon

- Optimize GUI buttons

- Work on sending/receiving multiple files (.zip?, Werkzeug send compresssed file functionality?)

- Make send file reselectable while server is already running

- Package app into an executable (for Windows, Linux, and Mac)
