
; (function (loft) {
    /** @type {HTMLFormElement} */
    const upload = document.querySelector('form#upload');
    /** @type {HTMLInputElement} */
    const fileSelector = upload.querySelector('#file-selector');
    /** @type {HTMLFieldSetElement} */
    const toSendList = upload.querySelector('#to-send');

    upload.addEventListener('submit', async function (e) {
        e.preventDefault();
        if (fileSelector.files.length <= 0) {
            loft.displayMessage('upload', 'failure', 'No file selected!');
            return;
        }

        /** @type {boolean} */
        const success = await loft.send(new FormData(this), uploadFailureCallback);

        if (success) {
            const msg = (fileSelector.files.length > 1 ? 'Files' : 'File') + ' sent successfully!';
            loft.displayMessage('upload', 'success', msg);
        }
    });

    fileSelector.addEventListener('change', function (_e) {
        for (const bubble of toSendList.querySelectorAll('.selected-file')) {
            toSendList.removeChild(bubble);
        }

        for (const file of fileSelector.files) {
            /** @type {HTMLElement} */
            const bubble = loft.createBubble(file.name);
            bubble.classList.add('selected-file');
            toSendList.append(bubble);
        }
    });

    /** @type {import('./api').ResponseFailureCallback} */
    function uploadFailureCallback(code, msg) {
        loft.displayMessage('upload', 'failure', code + ': ' + msg);
    }

})(globalThis.loft);
