
import './js/upload.js';
import { updateFileList } from './js/download.js';


updateFileList();
// update the file list periodically
setInterval(updateFileList, 1_000);
