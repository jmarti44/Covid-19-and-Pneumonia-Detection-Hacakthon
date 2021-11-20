import json
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from flask.scaffold import _matching_loader_thinks_module_is_package
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
    normal_convert = data["assemble"][0]["normal"]
    covid_convert = data["assemble"][0]["covid"]
    pneumonia_convert = data["assemble"][0]["pneumonia"]
    return render_template('/doctor.html', name = name, normal=normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)


@app.route('/patient.html')
def patient():
    return render_template("patient.html")

# @app.route('/test.html')
# def upload():
#     return render_template('test.html')

# @app.route('/doctor.html', methods=['GET','POST'])
# def doctor():
#     return render_template('doctor.html')

@app.route('/upload.html',methods = ['GET','POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filename = "covidTest.png"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return "File Uploaded Successfully"

