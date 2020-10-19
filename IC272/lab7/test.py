from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from scipy.stats import multivariate_normal as mnorm

data = pd.read_csv("data.csv")
Y = np.array(data["Z_Scratch"])
data.drop(columns=["Z_Scratch"])
print(data)
X = np.array(data)
X_train,X_test,Y_train,Y_test = tts(X,Y,random_state=42,test_size=0.3)

def kmeans(x_train,y_train,q):
    mdl = KMeans(n_clusters=q,random_state=42,)
    mdl.fit(x_train,y_train)
    return mdl

mdl = kmeans(X_train,Y_train,2)

class_mp = {}

for i in range(len(X_train)):
    try:
        class_mp[Y_train[i]].append(X_train[i])
    except:
        class_mp[Y_train[i]] = [X_train[i]]

def getcov(kms,X):
    means = kms.cluster_centers_
    l = []
    for mean in means:
        l.append(mean)
    
    d = {}
    print(kms.cluster_centers_)
    for i in range(len(X)):
        print(X[i])
        y = kms.predict([X[i]])
        print(y)
        try:
            d[l.index(y)].append(X[i])
        except:
            d[l.index(y)] = [X[i]]
    
    covmap = {}

    for k in d.keys():
        covmap[k] = np.cov(d[k])
    return [covmap,l]


kys = list(class_mp.keys())
for i in range(len(kys)):
    kms = kmeans(class_mp[kys[i]],len(class_mp[kys[i]])*[kys[i]],3)
    covmap,l = getcov(kms,class_mp[kys[i]])
    print(kms.cluster_centers_)
