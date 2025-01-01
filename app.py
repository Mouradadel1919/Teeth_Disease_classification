from __future__ import division, print_function
# coding=utf-8

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Keras
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model
import keras.utils as image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__, static_folder='static', template_folder='templates')
MODEL_PATH = './vgg16_model.h5'

# Load your trained model
model = load_model(MODEL_PATH)

#function for processing the input image abd prediction

def model_predict(img_path, model):

    # Preprocessing the image
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.image.resize(img, [224,224])
    img = img/255.0

    y = model.predict(img)

    return np.argmax(y)

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        if not os.path.exists("/app/uploads"):
            os.makedirs("/app/uploads")
        file_path = os.path.join('/app/uploads', secure_filename(f.filename))

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, model)
        

        # Process your result for human
        dic= {0:"CaS", 1:"CoS", 2:"Gum", 3:"MC", 4:"OC", 5:"OLP", 6:"OT"}

        pred_class = dic[preds]
        return pred_class
    return render_template('predict.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

