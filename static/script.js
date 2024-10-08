function convertSvg() {
    const svgCode = document.getElementById('svgCode').value;
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.style.display = 'none'; // Hide error message initially

    // Make a POST request to the server to convert SVG to PNG
    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `svg_code=${encodeURIComponent(svgCode)}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Show the image preview
        const img = document.getElementById('imagePreview');
        img.src = data.image;
        img.style.display = 'block';

        // Update the download link
        const downloadLink = document.getElementById('downloadLink');
        downloadLink.href = data.image;
        downloadLink.setAttribute('download', 'output.png');
        downloadLink.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.style.display = 'block'; // Show error message
    });
}