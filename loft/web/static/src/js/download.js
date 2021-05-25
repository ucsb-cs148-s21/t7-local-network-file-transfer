
import { receive, list } from './api.js';
import { displayMessage } from './ui.js';

/** @type {HTMLFormElement} */
export const download = document.querySelector('form#download');

download.addEventListener('submit', function (e) {
    e.preventDefault();

    const data = new FormData(this);
    /** @type {FormDataEntryValue[]} */
    const selected = data.getAll('selection');
    if (selected.length < 1) {
        displayMessage('download', 'failure', 'No files selected!');
    } else {
        receive(selected);
    }
});

/**
 * Tracks which file IDs are currently being displayed on the UI.
 * @type {Set<number>}
 */
const existing = new Set();

/** @type {HTMLFieldSetElement} */
const fileList = download.querySelector('fieldset#available');
export function updateFileList() {
    list(downloadFailureCallback).then(available => {
        if (available === null) return;

        /** @type {NodeListOf<HTMLElement>} */
        const listings = fileList.querySelectorAll('.download-listing-container');
        for (const listing of listings) {
            // clear existing entries no longer available
            if (!available.has(+listing.dataset.fileId)) {
                fileList.removeChild(listing);
                existing.delete(+listing.dataset.fileId);
            }
        }

        for (const [id, name] of available) {
            if (!existing.has(id)) {
                fileList.append(generateListing(name, id));
                existing.add(id);
            }
        }
    }).catch(err => {
        if (err instanceof NetworkError) {
            // TODO: disable the UI when the other side isn't present
        }
    });
}


/**
 * Generates a listing for the given file and file ID.
 * @param {string} filename - Name of the file to list.
 * @param {number} fileId - ID of the file.
 * @returns {HTMLElement} The listing for the file.
 */
function generateListing(filename, fileId) {
    /** @type {HTMLDivElement} */
    const container = document.createElement('div');
    container.classList.add('download-listing-container');
    container.dataset.fileId = fileId;

    /** @type {HTMLLabelElement} */
    const label = document.createElement('label');
    label.classList.add('button');
    label.classList.add('button-secondary');
    label.classList.add('download-listing');
    label.title = `Receive ${filename}`
    label.textContent = filename;
    label.htmlFor = 'download-selection-' + fileId;

    /** @type {HTMLInputElement} */
    const checkbox = document.createElement('input');
    checkbox.id = 'download-selection-' + fileId;
    checkbox.type = 'checkbox';
    checkbox.name = 'selection';
    checkbox.value = fileId;
    checkbox.tabIndex = 0;

    container.append(checkbox);
    container.append(label);

    return container;
}

/** @type {import('./api').ResponseFailureCallback} */
function downloadFailureCallback(code, msg) {
    displayMessage('download', 'failure', code + ': ' + msg);
}
