from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
import cv2

app = Flask(__name__)
model = load_model('densenet201_model.h5')

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    return img

def predict_deepfake(image_path):
    img = preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    if prediction[0][0] > 0.5:
        return "Deepfake"
    else:
        return "Real"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    file_path = 'temp.jpg'
    file.save(file_path)
    result = predict_deepfake(file_path)
    return result

if __name__ == '__main__':
    app.run(debug=True)
