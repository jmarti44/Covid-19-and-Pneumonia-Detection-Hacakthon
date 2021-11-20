import json
from flask import *
from flask import render_template
from keras.models import load_model
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
# app.config['SECRET_KEY'] = random_key

result = []

f = open("data.json",)
data = json.load(f)

for i in data["assemble"]:
    print(i)
    result.append(i)

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

    # normal_convert = data["assemble"][0]["normal"]
    # covid_convert = data["assemble"][0]["covid"]
    # pneumonia_convert = data["assemble"][0]["pneumonia"]
    normal_convert = 0
    covid_convert = 0
    pneumonia_convert = 0
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

    name = request.args.get('name')
    file = request.files['file']
    filename = secure_filename(file.filename)
    filename = "covidTest.png"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

    normal_convert = data["assemble"][0]["normal"]
    covid_convert = data["assemble"][0]["covid"]
    pneumonia_convert = data["assemble"][0]["pneumonia"]
    return render_template('/doctor.html', name = name, normal=normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)


