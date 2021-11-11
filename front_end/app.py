from flask import Flask ,render_template, request
import pandas as pd

app = Flask(__name__)

def drop():
    df=pd.read_csv("./static/symptoms.csv")
    p=""
    for x in df["Symptoms"]:
        p= p + "<option value='" + x + "'>" + x + "</option>"
    return p

dropdown=drop()

def mapdata():
    df=pd.read_csv("./static/symptoms.csv")
    map_value={}
    count=0
    for x in df["Symptoms"]:
        map_value[x]=count
        count=count+1

    return map_value

map_data=mapdata()

@app.route("/")
def hello_world():
    return render_template('index.html',dropdown=dropdown)

@app.route("/predict", methods =["GET", "POST"])
def predict():
    if request.method == "POST":
       S1 = request.form.get("ds1") 
       S2 = request.form.get("ds2")
       S3 = request.form.get("ds3") 
       S4 = request.form.get("ds4") 
       S5 = request.form.get("ds5") 
       S6 = request.form.get("ds6") 

       return "Your Symptoms are "+S1 + ","+S2 + ","+S3 + ","+S4 + ","+S5 + ","+S6 +".D"
    return render_template('index.html',dropdown=dropdown)





if __name__ == '__main__':
 	app.run(debug=True)