
import { send } from './api.js';
import { createBubble, displayMessage } from './ui.js';

/** @type {HTMLFormElement} */
export const upload = document.querySelector('form#upload');
/** @type {HTMLInputElement} */
const fileSelector = upload.querySelector('#file-selector');
/** @type {HTMLFieldSetElement} */
const toSendList = upload.querySelector('#to-send');

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
    for (const bubble of toSendList.querySelectorAll('.selected-file')) {
        toSendList.removeChild(bubble);
    }

    for (const file of fileSelector.files) {
        /** @type {HTMLElement} */
        const bubble = createBubble(file.name);
        bubble.classList.add('selected-file');
        toSendList.append(bubble);
    }
});

/** @type {import('./api').ResponseFailureCallback} */
function uploadFailureCallback(code, msg) {
    displayMessage('upload', 'failure', code + ': ' + msg);
}
