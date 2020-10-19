import sklearn
from sklearn.metrics import confusion_matrix,accuracy_score
import pandas as pd
from sklearn import preprocessing
from sklearn import model_selection
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import statistics as st
data=pd.read_csv("data.csv")
columns=data.columns
def classify(d):
    class0=d.loc[d[d.columns[len(d.columns)-1]] == 0]
    class1=d.loc[d[d.columns[len(d.columns)-1]] == 1]
    return class0,class1
def standardize(d):
    x = d.values #returns a numpy array
    min_max_scaler = preprocessing.StandardScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    d = pd.DataFrame(x_scaled)
    d.columns=columns
    d['Z_Scratch']=data['Z_Scratch']
    return d
def normalize(d):
    x = d.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    d = pd.DataFrame(x_scaled)
    d.columns=columns
    d['Z_Scratch']=data['Z_Scratch']
    return d
def splt(d):
    c0,c1=classify(d)
    train1,test1=model_selection.train_test_split(c0,test_size=.3,random_state=42,shuffle=True)
    train2,test2=model_selection.train_test_split(c1,test_size=.3,random_state=42,shuffle=True)
    train=pd.concat([train1,train2],ignore_index=True)
    test=pd.concat([test1,test2],ignore_index=True)
    train=pd.DataFrame(train)
    test=pd.DataFrame(test)
    train.columns=columns
    test.columns=columns
    return train,test
def Kclass(d,k):
    tr,te=splt(d)
    c=tr['Z_Scratch'].tolist()
    actual=te['Z_Scratch'].tolist()
    del tr['Z_Scratch']
    del te['Z_Scratch']
    neigh=KNeighborsClassifier(n_neighbors=k)
    neigh.fit(np.array(tr.values),c)
    pred=list(neigh.predict(np.array(te.values)))
    print("FOR K = ",k,sep='')
    print(confusion_matrix(actual,pred))
    print("ACCURACY - ",accuracy_score(actual,pred),end='\n\n')
    return accuracy_score(actual,pred)

def main():# amin
    acc=[]
    kk=[]
    for i in range(1,22,2):
        acc.append(Kclass(data,i))
        kk.append(i)
    print("Maximum Accuracy for k value - ",kk[acc.index(max(acc))],"Max ACC. = ",max(acc))
    plt.plot(kk,acc)
    plt.show()
    acc=[]
    kk=[]
    for i in range(1,22,2):
        acc.append(Kclass(normalize(data),i))
        kk.append(i)
    print("Maximum Accuracy for k value(NORMALIZED) - ",kk[acc.index(max(acc))],"Max ACC. = ",max(acc))
    plt.plot(kk,acc)
    plt.show()
    acc=[]
    kk=[]
    for i in range(1,22,2):
        acc.append(Kclass(standardize(data),i))
        kk.append(i)
    print("Maximum Accuracy for k value (Standardized)- ",kk[acc.index(max(acc))],"Max ACC. = ",max(acc))
    plt.plot(kk,acc)
    plt.show() 
    
if __name__ == "__main__":
    main()