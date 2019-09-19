import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from models import kNN
from models import linear_regretion as lr

#k = int(input("Enter k: "))

data = [[np.random.choice([0,1,2,3,4,5,6,7,8,9]),np.random.choice([0,1,2,3,4,5,6,7,8,9])] for i in range(60)]
data.extend([[100*np.random.choice([0,1,2,3,4,5,6,7,8,9]),100*np.random.choice([0,1,2,3,4,5,6,7,8,9])] for i in range(60)])
data.append([2,0])
target = 60*["s"]
target.extend(60*["l"])
target.append("s")

s = set(target)
d = {}
d2 = {}
k = 1
for v in target:
    if(v not in d.keys()):
        d[v] = k
        d2[k] = v
        k+=1

targetmod = []

for t in target:
    targetmod.append(d[t])

obj = kNN(3)

obj.fit(data,targetmod)
obj.plotAcc(50)
