import os
from uuid import uuid4
from flask import Flask, redirect, request, jsonify
from werkzeug.utils import secure_filename
import sys
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Config
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model('./model/model.h5')

@app.route('/')
def index():
    return jsonify({"message" : "NutriSight API v0.1.0 : Request Success"}), 200

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict(model, image):
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return np.argmax(prediction, axis=1)[0]

@app.route('/predict', methods=['POST'])
def post_predict():
    # print(request, file=sys.stdout)
    if 'file' not in request.files :
        return jsonify({"message": "Please insert image"}), 400
    
    file = request.files['file']
    
    if file.filename == '' :
        return jsonify({"message": "Please insert image"}), 400
    
    if file and allowed_file(file.filename):
        rand_name = uuid4().hex
        file_extension = os.path.splitext(file.filename)[1]
        filename = secure_filename(''.join([rand_name, file_extension]))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Image
    img_path = ''.join(['uploads/', filename])
    image = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
    
    prediction = predict(model, image)
    print(f'Predicted class: {prediction}', file=sys.stdout)

    return jsonify({"message" : "Success", "prediction" : str(prediction)}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 