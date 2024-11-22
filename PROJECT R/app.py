import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = r"C:\Users\Animesh Parida\OneDrive\Desktop\PROJECT R\model\retinopathy_model.keras"
model = load_model(MODEL_PATH)

# Define image size for the model input
IMAGE_SIZE = (512, 512)

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    img_file = request.files['image']
    img_path = os.path.join('uploads', img_file.filename)
    img_file.save(img_path)


    # Preprocess the image for model prediction
    img = cv2.imread(img_path)
    img = cv2.resize(img, IMAGE_SIZE)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize the image

    # Get prediction from the model
    prediction = model.predict(img)
    prediction = model.predict(img)
    severity_index = np.argmax(prediction[0])
    classes = ["Mild", "Moderate", "Severe"]
    severity = classes[severity_index]
    print(f"Predicted Severity: {severity}")
    
    # Get the index of the highest probability
    severity_index = np.argmax(prediction[0])
    severity = classify_severity(severity_index)

    return jsonify({"severity": severity})

def classify_severity(index):
    """Convert model output index to severity classification."""
    classes = ["Mild", "Moderate", "Severe"]
    return classes[index]

if __name__ == '__main__':
    # Ensure the uploads folder exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(debug=True)

app.run(debug=True, port=8000)


