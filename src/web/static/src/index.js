let fileInput = document.querySelector('#file-selector');
fileInput.onchange = function(e){
    let filename = fileInput.files[0].name;
    let newDiv = document.createElement("div");
    newDiv.innerHTML= `${filename} selected.`;
    newDiv.className = 'button file';
    document.querySelector('#file-selector-div').parentNode.insertBefore(newDiv,document.querySelector('#file-selector-div').nextSibling);
    console.log("hello");
    //document.querySelector('#file-selector-label').innerHTML=`${filename} selected.`;
}