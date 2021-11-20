from flask import Flask



app = Flask(__name__)

@app.route('/')
def index():
    testing = "landing"
    return testing

@app.route('/doctor.html')
def doctor():
    testing = "doctor page"
    return testing

@app.route('/patient.html')
def patient():
    testing = "patient page"
    return testing