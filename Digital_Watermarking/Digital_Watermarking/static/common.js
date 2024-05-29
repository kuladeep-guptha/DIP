function previewImage(input, previewId) {
    const preview = document.getElementById(previewId);
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.readAsDataURL(input.files[0]);
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        }
        
    } else {
        preview.src = "#";
        preview.style.display = 'none';
    }
}


document.getElementById('input_img').addEventListener('change', function() {
    previewImage(this, 'inputImgPreview');
});