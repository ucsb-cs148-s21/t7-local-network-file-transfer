let fileInput = document.querySelector('#file-selector');
fileInput.onchange = function(e){
    let filename = fileInput.files[0].name;
    document.querySelector('#file-selector-label').innerHTML=`${filename} selected.`;
}