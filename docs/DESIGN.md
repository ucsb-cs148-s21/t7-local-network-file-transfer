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


![design](https://user-images.githubusercontent.com/59618726/118883982-c12f8480-b8aa-11eb-9d07-f3399a9d1086.png)

## UI Design ##
The native UI is designed to imitate the functionality of native applications, such as with the use of grayed-out buttons to indicate non-interactivity and the ellipses `…` suffix to indicate that clicking a button will open an additional menu.

On the web UI, buttons for upload and download are grouped with blue boxes. "Submit" actions are indicated with a high-contrast green, while secondary actions needed before the submit action are colored in lower contrast blue. Interactive elements are shown with a drop shadow, and focus (for keyboard interaction) is indicated with a dotted border. All colors are chosen for at least 3:1 contrast with their backgrounds. The two groups are designed symmetrically to simplify user effort.

![Web UI](https://user-images.githubusercontent.com/55780596/120048717-b2448280-bfcc-11eb-856d-5b98605fcd34.png)


