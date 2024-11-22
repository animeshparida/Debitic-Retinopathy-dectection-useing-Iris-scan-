document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData();
    const imageFile = document.getElementById('imageInput').files[0];

    if (!imageFile) {
        document.getElementById('error').innerText = "Please select an image file.";
        return;
    }

    // Show image preview
    const imagePreview = document.getElementById('imagePreview');
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        imagePreview.classList.remove('hidden');
    };
    reader.readAsDataURL(imageFile);

    // Clear previous errors
    document.getElementById('error').innerText = "";
    document.getElementById('result').innerText = "Processing...";

    formData.append('image', imageFile);

    try {
        // Send the image to the backend
        const response = await fetch('http://127.0.0.1:5000/classify', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Failed to classify image. Please try again.');
        }

        const data = await response.json();

        // Display the result
        document.getElementById('result').innerText = `Severity: ${data.severity}`;
    } catch (error) {
        document.getElementById('result').innerText = "";
        document.getElementById('error').innerText = error.message;
    }
});
