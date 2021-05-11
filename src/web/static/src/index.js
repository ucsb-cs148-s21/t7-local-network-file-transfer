
/**
 * Display feedback to the user for upload/download.
 * @param {string} which - Either 'upload' or 'download', depending on which
 *      field to display the message for.
 * @param {string} type - The type of message--either 'success' or 'failure'.
 * @param {string} msg - The message to display.
 */
function displayMessage(which, type, msg) {
    if (which !== 'upload' && which !== 'download') return;

    /** @type {HTMLDivElement} */
    const display = document.querySelector(`#${which}-msg`);
    switch (type) {
        case 'success':
            display.classList.remove('error');
            display.classList.add('success');
            break;
        case 'failure':
            display.classList.remove('success');
            display.classList.add('error');
            break;
        default:
            return;
    }

    display.innerText = msg;
    clearDisplay(which, 2500);
}

/**
 * Clear the display after the given delay in ms.
 * @param {string} which - Either 'upload' or 'download', depending on which
 *      field to display the message for.
 * @param {number} after - How many ms to wait before clearing the display.
 */
function clearDisplay(which, after) {
    /** @type {HTMLDivElement} */
    const display = document.querySelector(`#${which}-msg`);

    setTimeout(() => {
        display.classList.remove('success');
        display.classList.remove('error');
        display.innerText = '';
    }, after);
}

/** @type {HTMLFormElement} */
const upload = document.querySelector('form#upload');
upload.addEventListener('submit', function (e) {
    e.preventDefault();
    /** @type {HTMLInputElement} */
    const fileSelector = document.querySelector('#file-selector');
    if (fileSelector.files.length <= 0) {
        displayMessage('upload', 'failure', 'No file selected!');
        return;
    }

    fetch('/api', {
        method: 'POST',
        body: new FormData(this),
    }).then(response => {
        if (response.status === 200) {
            const msg = (fileSelector.files.length > 1 ? 'Files' : 'File') + ' sent successfully!';
            displayMessage('upload', 'success', msg);
        } else {
            displayMessage('upload', 'success', `${response.status}: ${response.statusText}`);
        }
    });
});

/** @type {HTMLFormElement} */
const download = document.querySelector('form#download');
download.addEventListener('submit', function (e) {
    e.preventDefault();

    // TODO: get the file id from file list
    const id = 0;

    // Generate an anchor element with the `download` attribute and use that to
    // send the GET request to the api.
    const a = document.createElement('a');
    a.href = '/api?id=' + id;
    a.download = true;

    a.click();
});


function updateFileList() {
    fetch('/api', {
        method: 'LIST',
    })
        .then(response => response.json())
        .then(data => {
            for (const key of Object.keys(data.available)) {
                // const radio = document.createElement('input',)
                // download.childNodes.push(radio);
            }
        });
}

// update the file list periodically
setInterval(updateFileList, 100_000);
