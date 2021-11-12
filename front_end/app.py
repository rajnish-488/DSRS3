from flask import Flask ,render_template, request
import pandas as pd
from model_predict.predict import *

app = Flask(__name__)

def drop():
    df=pd.read_csv("./static/symptoms.csv")
    p=""
    for x in df["Symptoms"]:
        p= p + "<option value='" + x + "'>" + x + "</option>"
    return p

dropdown=drop()


@app.route("/")
def hello_world():
    return render_template('index.html',dropdown=dropdown)

@app.route("/predict", methods =["GET", "POST"])
def predict():
    if request.method == "POST":
        l=[]
        l.append(request.form.get("ds1")) 
        l.append(request.form.get("ds2"))
        l.append(request.form.get("ds3"))
        l.append(request.form.get("ds4"))
        l.append(request.form.get("ds5"))
        l.append(request.form.get("ds6")) 
        data=predict_disease(l)

        return "Your Disease is "+data[0] + ","+data[1] + ","+data[2] + ","+data[3]+ ","+data[4] + ","+data[5] +"."
    return render_template('index.html',dropdown=dropdown)





if __name__ == '__main__':
 	app.run(debug=True)