import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg, sqrt
from sklearn.model_selection import train_test_split as tts
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures as PF

def extractAttribute(data, features, target):
    Y = np.array(data[target])
    X = np.array(data[features])
    return X, Y

def insert(X):
    X = list(X)
    for i in range(len(X)):
        X[i] = list(X[i])
        X[i].append(1)
    return np.array(X)

class linear_regretion(object):

    def __init__(self):
        pass
        
    def fit(self,X,Y):
        self.x_train, self.x_test,self.y_train, self.y_test = tts(X,Y,test_size=.3,random_state=42,shuffle=True)  
        self.w = linalg.solve(np.dot(self.x_train.T,self.x_train),np.dot(self.x_train.T,self.y_train))

    def predict(self,x):
        x = np.array(x)
        return np.dot(x,self.w)

    def get_RMSE(self):
        rmse = 0
        for i,x in enumerate(self.x_test):
            rmse += (self.y_test[i] - self.predict(x))**2
        return sqrt(rmse/len(self.x_test))

    def polynomalize(self,degree):
        pf = PF(degree=degree)
        self.x_train = pf.fit_transform(self.x_train)
        print(self.x_train[0])
        self.w = linalg.solve(np.dot(self.x_train.T,self.x_train),np.dot(self.x_train.T,self.y_train)) 
        
class polynomialRegression:

    def __init__(self):
        pass
        
    def fit(self,X,Y,degree):
        self.x_train, self.x_test,self.y_train, self.y_test = tts(X,Y,test_size=.3,random_state=42,shuffle=True)  
        self.pf = PF(degree=degree)
        self.x_train = self.pf.fit_transform(self.x_train)
        self.x_test = self.pf.fit_transform(self.x_test)
        self.w = linalg.solve(np.dot(self.x_train.T,self.x_train),np.dot(self.x_train.T,self.y_train)) 

    def predict(self,x):
        return np.dot(x,self.w)

    def get_RMSE(self):
        rmse = 0
        self.y_obs = []
        for i,x in enumerate(self.x_test):
            y = self.predict(x)
            rmse += (self.y_test[i] - y)**2
            self.y_obs.append(y)
        return sqrt(rmse/len(self.x_test))

    def get_RMSE_train(self):
        rmse = 0
        self.y_obs = []
        for i,x in enumerate(self.x_train):
            y = self.predict(x)
            rmse += (self.y_train[i] - y)**2
        return sqrt(rmse/len(self.x_train))

    def plot2D(self):
        for x in self.x_test:
            d = self.predict(x)
            plt.scatter(x[1],d,color="black")
        plt.show()
    





    