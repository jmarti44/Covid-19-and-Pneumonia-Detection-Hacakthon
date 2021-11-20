from flask import Flask
from flask import render_template
from flask import request
from werkzeug.wrappers import request




app = Flask(__name__)

@app.route('/')
def index():
    #testing = "landing"
    return render_template('test.html')

@app.route('/doctor.html')
def doctor():
    #testing = "doctor page"
    return render_template('doctor.html')

@app.route('/patient.html')
def patient():
    testing = "patient page"
    return render_template("patient.html")

@app.route('/image.html')
def upload():
    if request.method == 'POST':
        print('upload called')