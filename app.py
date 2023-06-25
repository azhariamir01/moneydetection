from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import torch

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    # get image from request
    try:
        image = request.files['image']
    except (KeyError, FileNotFoundError, IOError):
        return render_template('error.html', error="Error accessing the uploaded file")

    objects = detect_objects(image)

    # if the function returned only a string, that means an error has occurred, and we treat it as such
    if isinstance(objects, str):
        return render_template('error.html', error=objects)
    else:
        return render_template('result.html', total=objects[0], objects=objects[1:])


def detect_objects(image):
    '''
    This function takes as input an image, and returns a list with the predictions from the model
    :param image: The image to be used for object detection
    :return: list of predictions from the model, or string containing error log
    '''

    try:
        # load the YOLOv5s model and set it to evaluation
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt')
        model.eval()
    except (ImportError, RuntimeError):
        return ["Error occurred while loading the model"]

    try:
        # open the uploaded image file
        image_pil = Image.open(image)
        width, height = image_pil.size
    except (FileNotFoundError, IOError):
        return ["Error accessing or reading the image file"]

    if width != 640 or height != 640:

        try:
            # resize the image to the models expected input shape if needed
            resized_image = image_pil.resize((640, 640))
        except (ValueError, AttributeError):
            return "Invalid image object for resizing"
    else:
        resized_image = image_pil

    try:
        # perform object detection on the image using our model
        results = model(resized_image)
    except (TypeError, RuntimeError, AttributeError):
        return "Error occurred during model prediction"

    # get detected objects and labels
    results_df = results.pandas().xyxy[0]
    bills = results_df['name'].tolist()

    objects = []

    if len(bills) == 0:
        # if no objects were detected treat it as such
        objects.append("0 RON")
        objects.append("No bills detected")

    else:
        # if bills were detected, count occurrences and total sum
        bills_int = [int(item) for item in bills]

        value_counts = Counter(bills_int)
        sorted_counts = sorted(value_counts.items(), key=lambda x: int(x[0]), reverse=True)

        objects.append(f"{sum(bills_int)} RON")
        for value, count in sorted_counts:
            # add the count and value to the list
            if count > 1:
                objects.append(f"{count} bills of {value} RON")
            else:
                objects.append(f"{count} bill of {value} RON")

    return objects


if __name__ == '__main__':
    app.run()
