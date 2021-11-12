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

def map_weight():
    df=pd.read_csv("./static/sever.csv")
    map_weight={}
    for x,y in zip(df["Symptom"],df["weight"]):
        x=" "+x
        map_weight[x]=y
    return map_weight
map_weight=map_weight()


def predict_disease(l):
    count=0
    sumvalue=0
    slist=[0]*131
    for x in l:
        if x != "Select Symptoms":
            slist[map_data2[x]]=1
            if x in map_weight:
                sumvalue=sumvalue+map_weight[x]
                count=count+1

    disease=map_data[(np.argmax(model.predict([slist]), axis=-1))[0]]
    out=mapvalue[disease]
    if(count!=0):
        level = sumvalue/count
    if level>0 and level<0.21:
        out.append("Common Symptoms take general medicine and contact the near by Doctor.")
        out.append("green")
    elif level>=0.21 and level<0.49:
        out.append("Moderate Symptoms, the state can be critical, contact near by Doctor.")
        out.append("blue")
    elif level>=0.49 and level<1:
        out.append("Cretical Symptoms, the worst state, immediatly reach a nearby Hospital.")
        out.append("red")
    return out