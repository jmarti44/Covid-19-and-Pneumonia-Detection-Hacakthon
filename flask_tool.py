from flask import Flask
from flask import render_template
from flask import request
# from werkzeug.wrappers import request


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

@app.route('/test.html')
def upload():
    return render_template('test.html')

@app.route('/image.html', methods=["POST", "GET"])
def success():
    if request.method == 'POST':
        return render_template('image.html')