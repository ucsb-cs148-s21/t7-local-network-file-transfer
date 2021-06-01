
; (function (global) {
    'use strict';
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
    global.displayMessage = displayMessage;

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

    /**
     * Create a non-interactive bubble for a file.
     * @param {string} name - file name
     * @returns {HTMLElement}
     */
    function createBubble(name) {
        if (name.length >= 24) {
            name = name.slice(0, 23) + '…';
        }

        const bubble = document.createElement('div');
        bubble.innerText = name;
        bubble.classList.add('bubble');
        return bubble;
    }

    if (global.loft === undefined) global.loft = {};
    Object.assign(global.loft, {
        displayMessage,
        clearDisplay,
        createBubble,
    });
})(globalThis);
