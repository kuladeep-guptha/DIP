function imageCompressionFrom(e){
    e.preventDefault()

    const form = document.getElementById('imgCompressionFrom');
    const formData = new FormData(form);
    const outputTitle = document.getElementById('outputTitle');
    const outputImg = document.getElementById('outputImg'); // Get the output image element
    const downloadLink = document.getElementById('downloadLink'); // Get the download link element

    // Get the elements for initial size, final size, and reduction
    const initialSizeElement = document.getElementById('initialSize');
    const finalSizeElement = document.getElementById('finalSize');
    const reductionElement = document.getElementById('reduction');

    fetch('/compress', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) 
    .then(data => {
        console.log(data);
        let output_path = data.output_path;
        let initial_size = data.initial_size;
        let final_size = data.final_size;
        let reduction = data.reduction;

        if (outputTitle.classList.contains('hide')) {
            outputTitle.classList.remove('hide');
        }

        outputImg.src = '#';
        outputImg.src = output_path + '?timestamp=' + new Date().getTime();
        if (outputImg.classList.contains('hide')) {
            outputImg.classList.remove('hide');
        }

        downloadLink.href = output_path;
        if (downloadLink.classList.contains('hide')) {
            downloadLink.classList.remove('hide');
        }

        const initialSizeKB = (initial_size / 1024).toFixed(1);
        const finalSizeKB = (final_size / 1024).toFixed(1); 

        initialSizeElement.textContent = "Initial size: "+ initialSizeKB + "KB";
        if (initialSizeElement.classList.contains('hide')) {
            initialSizeElement.classList.remove('hide');
        }

        finalSizeElement.textContent = "Final size: " + finalSizeKB + "KB";
        if (finalSizeElement.classList.contains('hide')) {
            finalSizeElement.classList.remove('hide');
        }

        reductionElement.textContent = "Size reduced by: " + reduction.toFixed(2) + "%";
        if (reductionElement.classList.contains('hide')) {
            reductionElement.classList.remove('hide');
        }

        
        // Output the results
        console.log("Initial size:", initialSizeKB + "KB");
        console.log("Final size:", finalSizeKB + "KB");
        console.log("Size reduced by:", reduction.toFixed(2) + "%");
    })
    .catch(error => console.error('Error:', error));
}
