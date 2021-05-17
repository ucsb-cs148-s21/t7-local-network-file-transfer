# LOFT Architecture

- Router
  - Connects everything together
- Flask web server (Locally Hosted)
  - Serves the client webpage
  - API interfaces with the Host machine's file system for sending to the client and downloading files received by client.
- Host QT GUI
  - Allows for files to send to client from host to be selected.
- Client Webpage
  - Interfaces with the Client's file system for downloading and uploading
