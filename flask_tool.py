from flask import Flask
from flask import render_template
from flask import request
from werkzeug.wrappers import request




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctor.html')
def doctor():
    name = request.args.get('name')
    return render_template('doctor.html')

@app.route('/patient.html')
def patient():
    return render_template("patient.html")

@app.route('/image.html')
def upload():
    if request.method == 'POST':
        print('upload called')