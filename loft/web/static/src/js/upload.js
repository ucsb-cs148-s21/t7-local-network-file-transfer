
import { send } from './api.js';
import { displayMessage } from './ui.js';

/** @type {HTMLFormElement} */
export const upload = document.querySelector('form#upload');
/** @type {HTMLInputElement} */
const fileSelector = upload.querySelector('#file-selector');

upload.addEventListener('submit', async function (e) {
    e.preventDefault();
    if (fileSelector.files.length <= 0) {
        displayMessage('upload', 'failure', 'No file selected!');
        return;
    }

    /** @type {boolean} */
    const success = await send(new FormData(this), uploadFailureCallback);

    if (success) {
        const msg = (fileSelector.files.length > 1 ? 'Files' : 'File') + ' sent successfully!';
        displayMessage('upload', 'success', msg);
    }
});

fileSelector.addEventListener('change', function (_e) {
    for (const bubble of upload.querySelectorAll('.selected-file')) {
        upload.removeChild(bubble);
    }

    for (const file of fileSelector.files) {
        /** @type {string} */
        let filename = file.name;
        if (filename.length >= 24) {
            filename = filename.slice(0, 23) + '…';
        }

        const fileBubble = document.createElement('div');
        fileBubble.innerText = `${filename} selected.`;
        fileBubble.classList.add('bubble');
        fileBubble.classList.add('selected-file');
        fileSelector.parentNode.insertBefore(fileBubble, fileSelector);
    }
});

/** @type {import('./api').ResponseFailureCallback} */
function uploadFailureCallback(code, msg) {
    displayMessage('upload', 'failure', code + ': ' + msg);
}
