
/**
 * Callback for handling request failures.
 * @callback ResponseFailureCallback
 * @param {number} code - response status code
 * @param {string} msg - response status msg
 */

/** @type {ResponseFailureCallback} */
const responseFailureNoOp = (status, text) => { };

/**
 * Send all files from the given FormData.
 * @param {FormData} data - formdata with files to send
 * @param {ResponseFailureCallback} [onfail] - callback for failure responses
 * @returns {boolean} Whether or not the files uploaded successfully.
 */
export async function send(data, onfail = responseFailureNoOp) {
    /** @type {Response} */
    const response = await fetch('/api/files', { method: 'POST', body: data });
    if (response.status !== 200) {
        onfail(response.status, response.statusText);
        return false;
    } else {
        return true;
    }
}

/**
 * Get the requested file IDs.
 * @param {number[]} ids - File IDs to GET.
 */
export function receive(ids) {
    for (const id of ids) {
        // Generate an anchor element with the `download` attribute and use that to
        // send the GET request to the api.
        const a = document.createElement('a');
        a.href = '/api/files/' + id;
        a.download = true;

        a.click();
    }
}


/**
 * Get a listing of available file names and their IDs.
 * @param {ResponseFailureCallback} [onfail] - Handle response failures.
 * @returns {Map<number, string>?} Returns a mapping of file IDs to file names.
 */
export async function list(onfail = responseFailureNoOp) {
    /** @type {Response} */
    const response = await fetch('/api/files', { method: 'GET' });
    if (response.status != 200) {
        onfail(response.status, response.statusText)
        return null;
    } else {
        return new Map((await response.json()).available);
    }
}
