
document.getElementById('watermark').addEventListener('change', function() {
    previewImage(this, 'watermarkPreview');
});

function watermarkForm(e) {
    e.preventDefault()
    const form = document.getElementById('watermarkForm');
    const formData = new FormData(form);
    const outputTitle = document.getElementById('outputTitle');
    const outputImg = document.getElementById('outputImg');
    const downloadLink = document.getElementById('downloadLink');

    fetch('/', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
    .then(data => {
        console.log(data)
        let img_b64 = data.output_img
        if (outputTitle.classList.contains('hide')) {
            outputTitle.classList.remove('hide');
        }

        outputImg.src = 'data:image/jpeg;base64,' + img_b64;
        if (outputImg.classList.contains('hide')) {
            outputImg.classList.remove('hide');
        }
        
        downloadLink.href = 'data:image/jpeg;base64,' + img_b64;
        if (downloadLink.classList.contains('hide')) {
            downloadLink.classList.remove('hide');
        }


    }).catch(error => {
        console.log(error)
    });
}
