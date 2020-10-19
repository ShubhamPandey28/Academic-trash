import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from model import *


data = pd.read_csv("data.csv")
 
Y = list(data["Force"])

rmse = []

for i in range(1,69):
    X = constFeatures(i,Y)
    l = len(Y)-2*i
    lr = polynomialRegression()
    lr.fit(X,Y[:l],1)
    print("lag=",i)
    print("w=",lr.w)
    rmse.append(lr.get_RMSE())
    
print()
print()
print("====================================================")
print("OBSERVATION FROM THE DATASET:")
print("-----------------------------")
print("-> min RMSE value at lag =",rmse.index(min(rmse)))
print(rmse)
plt.plot(list(range(1,69)),rmse)
plt.show()
