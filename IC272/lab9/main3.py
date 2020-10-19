import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels as sm

from model import *

data = pd.read_csv("data.csv")
 
Y = list(data["Force"])

X = np.array(Y[1:len(Y)]).reshape((len(Y)-2,1))

lr = linear_regretion()
lr.fit(X,Y[:-2])
rmse = lr.get_RMSE()
print(rmse)

print("----------------------------------")

X1 = Y[1:1+len(Y)-4]
X2 = Y[2:2+len(Y)-4]

X = np.array([X1,X2])
X = X.T

lr = polynomialRegression()
lr.fit(X,Y[:len(Y)-4],1)
print(lr.get_RMSE())