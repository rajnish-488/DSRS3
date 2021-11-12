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

def dataout(data):
    return "<div style='text-align:center;'><div ><h2>The Predicted Disease</h2><h3>"+str(data[0])+"</h3></div><br><div><h2>Disease Discription</h2><h3>"+str(data[1])+"</h3></div><br><div><h3>"+str(data[6])+"</h3></div><br><div><h2>Pecaution to take</h2><h3>" +str(data[2])+ "</h3><h3>" + str(data[3]) + "</h3><h3>" + str(data[4]) + "</h3><h3>"+str(data[5])+"</h3></div></div>"


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

        return render_template('predict.html',data = data)
    return render_template('index.html',dropdown=dropdown)





if __name__ == '__main__':
 	app.run(debug=True)