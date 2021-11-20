from flask import Flask



app = Flask(__name__)

@app.route('/')
def index():
    testing = "doctor page"
    return testing