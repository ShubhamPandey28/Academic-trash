import pandas as pd
import numpy as np
from model import *
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
cov = data.corr()

m=0
col=""
for c in data.columns:
    covs = cov[c]
    i = list(data.columns).index(c)
    if i!=0 and i!=len(data.columns)-1:
        tmp = max(max(abs(covs[:i])),max(abs(covs[i+1:])))
    elif i==0:
        tmp = max(abs(covs[i+1:]))
    else:
        tmp = max(abs(covs[:i]))
    if(tmp > m):
        m = tmp
        col = c
print(col)
cols = list(data.columns)
def getcool(col):
    covcl = list(cov[col])
    try:
        cool = cols[covcl.index(max(max(cols[:cols.index(col)]),max(cols[cols.index(col)+1:])))]
    except:
        try:
            cool = cols[covcl.index(max(cols[:cols.index(col)]))]
        except:
            cool = cols[covcl.index(max(cols[cols.index(col)+1:]))]
    return cool

col2 = getcool(col)
print(col2)

X, Y = extractAttribute(data,data.columns,"quality")

