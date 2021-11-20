from keras.models import load_model
from flask import Flask, jsonify
from PIL import Image, ImageOps
import json
import numpy as np


    
def generate_Prediction(path):
    # Load the model
    model = load_model('keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
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
    

path = "images/covidTest.png" 
result = generate_Prediction(path)


normal_convert = result[0][0].item()
covid_convert = result[0][1].item()
pneumonia_convert = result[0][2].item()


print("normal: {0}".format(round(normal_convert, 3)))
print("covid: {0}".format(round(covid_convert, 3)))
print("pneumonia: {0}".format(round(pneumonia_convert, 3)))

prediction_data = {}
prediction_data["assemble"] = []
prediction_data["assemble"].append({
    "normal": round(result[0][0].item(), 3),
    "covid": round(result[0][1].item(), 3),
    "pneumonia": round(result[0][2].item(), 3)
})

with open('data.json', 'w') as output:
    json.dump(prediction_data, output)


