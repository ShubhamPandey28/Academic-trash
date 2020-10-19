import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")

X = data["Date"]
Y = data["Force"]
X = list(X)
Y = list(Y)

prev = []

for i in range(1,len(X)-1):
    prev.append(Y[i-1])
print(np.corrcoef(prev,Y[:-2]))