let fileInput = document.querySelector('#file-selector');
fileInput.onchange = function(e){
    let filename = fileInput.files[0].name;
    if(filename.length >= 8){
        filename = filename.slice(0,7) + '...';
    }
    if(!document.querySelector('#selected-file-1')){
        let newDiv = document.createElement("div");
        newDiv.id = "selected-file-1"
        newDiv.innerHTML= `${filename} selected.`;
        newDiv.className = 'selected-file';
        document.querySelector('#file-selector-div').parentNode.insertBefore(newDiv,document.querySelector('#file-selector-div').nextSibling);
    }
    else{
        let newDiv = document.querySelector('#selected-file');
        newDiv.innerHTML = `${filename} selected.`;
    }
}