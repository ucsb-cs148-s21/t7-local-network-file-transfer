
/**
 * Display feedback to the user for upload/download.
 * @param {string} which - Either 'upload' or 'download', depending on which
 *      field to display the message for.
 * @param {string} type - The type of message--either 'success' or 'failure'.
 * @param {string} msg - The message to display.
 */
export function displayMessage(which, type, msg) {
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
export function clearDisplay(which, after) {
    /** @type {HTMLDivElement} */
    const display = document.querySelector(`#${which}-msg`);

    setTimeout(() => {
        display.classList.remove('success');
        display.classList.remove('error');
        display.innerText = '';
    }, after);
}
