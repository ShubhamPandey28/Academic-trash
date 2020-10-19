import pandas as pd
import numpy as np
from model import *
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
X, Y = extractAttribute(data,data.columns,"quality")

rmseTrain = []
rmseTest = []

for p in range(1,6):
    regressor = polynomialRegression()
    regressor.fit(X,Y,p)
    rmsetrain = regressor.get_RMSE_train()
    rmsetest = regressor.get_RMSE()
    rmseTest.append(rmsetest)
    rmseTrain.append(rmsetrain)
    plt.title("p = "+str(p))
    plt.xlabel("y_test")
    plt.ylabel("y_obs")
    plt.scatter(regressor.y_test,regressor.y_obs)
    plt.show()
p = np.array(p)
plt.bar(p-0.1,rmseTest,width=0.1,color="blue")
plt.bar(p+0.1,rmseTrain,width=0.1,color="green")
plt.show()
    
