let fileInput = document.querySelector('#file-selector');
fileInput.onchange = function(e){
    let filename = fileInput.files[0].name;
    if(!document.querySelector('#selected-file')){
        let newDiv = document.createElement("div");
        newDiv.id = "selected-file"
        newDiv.innerHTML= `${filename} selected.`;
        newDiv.className = 'button file';
        document.querySelector('#file-selector-div').parentNode.insertBefore(newDiv,document.querySelector('#file-selector-div').nextSibling);
    }
    else{
        let newDiv = document.querySelector('#selected-file');
        newDiv.innerHTML = `${filename} selected.`;
    }
}