import os
from uuid import uuid4
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from google.cloud import storage
from google.oauth2 import service_account
from PIL import Image
import requests 
import numpy as np

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Config
app = Flask(__name__)

CREDENTIALS = service_account.Credentials.from_service_account_file(os.environ.get('CREDENTIAL_PATH'))
CLIENT = storage.Client(credentials=CREDENTIALS)
BUCKET = CLIENT.bucket(os.environ.get('BUCKET_NAME'))

model = load_model('./model/model.h5')

@app.route('/')
def index():
    return jsonify({"message" : "NutriSight API v1.0.0 : Request Success"}), 200

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
    if 'image' not in request.files :
        return jsonify({"message": "Please insert image"}), 400
    
    file = request.files['image']
    
    if file.filename == '' :
        return jsonify({"message": "Please insert image"}), 400
    
    # Upload to Bucket
    if file and allowed_file(file.filename):
        rand_name = uuid4().hex
        file_extension = os.path.splitext(file.filename)[1]
        filename = secure_filename(''.join([rand_name, file_extension]))
        destination_path = ''.join(['uploads/', filename])
        blob = BUCKET.blob(destination_path)
        generation_match_precondition = 0
        
        try :
            blob.upload_from_file(file, if_generation_match=generation_match_precondition)
            
        except :
            return jsonify({"message" : "Filename already exist"}), 400
        
    else :
        return jsonify({"message": "Unsuported file format"}), 400
    
    # Image Processing
    image = Image.open(file)
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
    
    try :
        # Get product
        prediction = predict(model, image)
        req_product = requests.get(os.environ.get('PRODUCT_SERVICE_URL') + '/' + str(prediction))
        req_product = req_product.json()
        
        return req_product, 200
    
    except:
        return jsonify({"message" : "Server error"}), 500
    

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
 