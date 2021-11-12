from keras.models import load_model
import numpy as np
import pandas as pd

model = load_model("network.h5")
df=pd.read_csv("./static/the_ANN_output.csv")
def creation_of_map(x):
    dicr={}
    count=0
    for a in x:
        dicr[count]=a
        count+=1
    return dicr
map_data=creation_of_map(df["Disease"])

df2=pd.read_csv("./static/detail_and_precation.csv")
mapvalue={}
for x,y,p1,p2,p3,p4 in zip(df2["Disease"],df2["Description"],df2["Precaution_1"],df2["Precaution_2"],df2["Precaution_3"],df2["Precaution_4"]):
    mapvalue[x]=[x,y,p1,p2,p3,p4]

def mapdata():
    df=pd.read_csv("./static/symptoms.csv")
    map_value={}
    count=0
    for x in df["Symptoms"]:
        map_value[x]=count
        count=count+1
    return map_value

map_data2=mapdata()


def predict_disease(l):
	slist=[0]*131
	for x in l:
		if l != "Select Symptoms":
			slist[map_data2[x]]=1
	disease=map_data[(np.argmax(model.predict([slist]), axis=-1))[0]]
	return mapvalue[disease]