from flask import Flask
import json
from flask import *
from script_python import kernel as K


app = Flask(__name__)
@app.route('/testing.html')
def index():
    testing = "testing from flask to vuejs"
    return render_template("test.html",testing=jsonify(**K.JSONResponse(data=testing, error=False, message='')))