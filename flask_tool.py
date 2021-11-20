import json
import tensorflow as tf
from flask import *
from flask import render_template
from keras.models import load_model
from werkzeug.utils import secure_filename
from sklearn.preprocessing import LabelEncoder
from flask import Flask, jsonify
from PIL import Image, ImageOps
import json
import numpy as np
import os
# from keras import model_from_json 




# loaded_model = model_from_json(loaded_model_json)
# loaded_model.load_weights("keras_model.h5")
# loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
# app.config['SECRET_KEY'] = random_key

result = []

# f = open("data.json",)
# data = json.load(f)

# for i in data["assemble"]:
#     print(i)
#     result.append(i)
# global graph,model
# model,graph = init()
# sys.path.append(os.path.abspath("./model"))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
# app.config['SECRET_KEY'] = random_key


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctor.html', methods=["POST", "GET"])
def doctor():

    name = request.args.get('name')
    # if request.method == "POST":

    normal_convert = 0
    covid_convert = 0
    pneumonia_convert = 0
    print('hello')
    return render_template('/doctor.html', name = name, normal=normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)



@app.route('/patient.html')
def patient():
    name = request.args.get('name')
    normal_convert = (data["assemble"][0]["normal"])*100
    covid_convert = (data["assemble"][0]["covid"])*100
    pneumonia_convert = (data["assemble"][0]["pneumonia"])*100
    return render_template('/patient.html', name = name, normal= normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)


@app.route('/image.html',methods = ['GET','POST'])
def upload():
    counter = 0
    name = request.args.get('name')
    file = request.files['file']
    filename = secure_filename(file.filename)
    filename = "covidTest{0}.png".format(counter)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    prediction = load("images/{0}".format(filename))
    print('prediction',prediction)
    normal_convert = round(prediction[0][0], 6) * 100
    covid_convert = round(prediction[0][1], 6) * 100
    pneumonia_convert = round(prediction[0][2], 6) * 100
    counter+=1
    return render_template('/doctor.html', name = name, normal=normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)
def load(path):
    model = load_model("keras_model.h5", compile=True)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(path)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = image.convert('RGB')
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # print(prediction)
    return prediction
