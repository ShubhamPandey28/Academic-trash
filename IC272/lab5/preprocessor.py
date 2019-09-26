import numpy as np
import sklearn.preprocessing as sp
from sklearn.model_selection import train_test_split as tts

def normalize(l):
    return sp.normalize(np.array(l))

def readCSV(filePath="data.csv"):
    Xs = []
    Ys = []
    with open(filePath,'r') as f:
        lines = f.readlines()

        for line in lines[1:]:
            l = list(map(float,line[:-1].split(",")))
            Xs.append(l[:-1])
            Ys.append(l[-1])    
    return Xs,Ys
    
def standardize(l):
    l = np.array(l)
    return sp.normalize(l,axis=1,norm="l1")


def splitter(inp,tg):
    d = {}
    for i in range(len(inp)):
        try:
            d[tg[i]].append(inp[i])
        except:
            d[tg[i]] = [inp[i]]
    train_data = []
    test_data = []
    for key in d.keys:
        td, tstd = tts(d[key],test_size=.3,random_state=42,shuffle=True)
        train_data.extend(td)
        test_data.extend(tstd)
    return [test_data,train_data]