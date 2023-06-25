function show_preview(event) {
    // initialize FileReader Object
    var reader = new FileReader();

    // define function for FileReader
    reader.onload = function(){
        // get preview element (by ID)
        var preview = document.getElementById('preview');

        // initialize new Image object
        var image = new Image();

        // Define the onload function for Image
        image.onload = function() {

            // create a canvas element
            var canvas = document.createElement('canvas');
            var context = canvas.getContext('2d');

            // set max width and height
            var maxWidth = 300;
            var maxHeight = 300;

            // get image width and height
            var width = image.width;
            var height = image.height;

            // resize image if needed (maintain aspect ratio)
            if (width > height) {
                if (width > maxWidth) {
                    height *= maxWidth / width;
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width *= maxHeight / height;
                    height = maxHeight;
                }
            }

            // set canvas dimensions to new width/height
            canvas.width = width;
            canvas.height = height;

            // draw the image and clear the preview element
            context.drawImage(image, 0, 0, width, height);
            preview.innerHTML = '';
            preview.appendChild(canvas);

            // call showResultButton method
            show_result_button();
        };
        image.src = reader.result;
    }
    // read uploaded file as data URL
    reader.readAsDataURL(event.target.files[0]);
}

function show_result_button() {
    // get element by result-btn ID
    var resultBtn = document.getElementById('result-btn');

    // set display property of result button
    resultBtn.style.display = 'inline-block';
}

// add event listener
document.getElementById('file-upload').addEventListener('change', function(event) {
    // call show_preview method
    show_preview(event);
});