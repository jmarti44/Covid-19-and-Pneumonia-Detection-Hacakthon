from flask import *
import json



app = Flask(__name__)

result = []

f = open("data.json",)
data = json.load(f)

for i in data["assemble"]:
    print(i)
    result.append(i)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctor.html', methods=["POST", "GET"])
def doctor():
    if request.method == "POST":
        normal_convert = result["normal"]
        covid_convert = result["covid"]
        pneumonia_convert = result["pneumonia"]
    return render_template('/templates/doctor.html', normal=normal_convert, covid=covid_convert, pneumonia=pneumonia_convert)

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