from flask import Flask
import json



app = Flask(__name__)

@app.route('/')
def index():
    testing = "testing from flask to vuejs"
    # return render_template("/",testing=jsonify(data=testing, error=False, message=''))
    return testing