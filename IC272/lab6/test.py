import pandas as pd
from sklearn.model_selection import train_test_split as tts
import numpy as np
data = pd.read_csv("data.csv")

def fit(dataframe,target_attribute):

    Y = dataframe[target_attribute]
    X = dataframe.drop(columns=[target_attribute])

    X_train, X_test, y_train, y_test = tts(X,Y,test_size=0.3, random_state=42)
    print(X_train,set(y_train))
    infoMatrix = [] #[[[m11,sig11],[m12,sig12]],[[m21,sig21],[m22,sig22]]]

fit(data,"class")

print(np.std([[1,2,3],[1,2,5],[5,23,1]],axis=1))


'''
def predict(self,x):
        lhds = []
        for j in range(len(self.key)):
            l = 0
            for i in range(len(x)):
                l += getGaussian(x[i],self.infoMatrix[j][i][0],self.infoMatrix[j][i][1])
            lhds.append(l)
        mx = lhds.index(max(lhds))
        return self.key[mx]
'''