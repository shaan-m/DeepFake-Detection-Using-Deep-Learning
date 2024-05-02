function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('preview');
        output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}

async function predict() {
    var fileInput = document.querySelector('input[type="file"]');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('image', file);

    var response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    var result = await response.text();
    document.getElementById('result').textContent = result;
}

async function preprocessAndPredict(imagePath) {
    var formData = new FormData();
    formData.append('image', imagePath);

    var response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    var result = await response.text();
    console.log("Result:", result);
}

