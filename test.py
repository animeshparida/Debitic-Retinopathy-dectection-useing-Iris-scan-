import numpy as np
from tensorflow.keras.models import load_model
import cv2

# Load the model
model = load_model('retinopathy_model.keras')

# Test on a sample image
img = cv2.imread(r'C:\Users\Animesh Parida\OneDrive\Desktop\ANIMESH\PHOTOS\PHOTO-removebg-preview.jpg')
img = cv2.resize(img, (512, 512))
img = np.expand_dims(img, axis=0) / 255.0

# Predict
prediction = model.predict(img)
severity_index = np.argmax(prediction[0])
classes = ["Mild", "Moderate", "Severe"]
severity = classes[severity_index]
print(f"Predicted Severity: {severity}")
