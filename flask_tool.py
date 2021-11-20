from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from flask.scaffold import _matching_loader_thinks_module_is_package
from werkzeug.utils import secure_filename
import os




# from werkzeug.wrappers import request



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
# app.config['SECRET_KEY'] = random_key

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctor.html')
def doctor():
    # name = request.args.get('name')
    return render_template('doctor.html')

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

