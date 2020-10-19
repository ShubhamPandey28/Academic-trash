from models import bayesClassifier as bc
import pandas as pd
from preprocessor import PCAtransform, standardize
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
effs = []
d = []

obj = bc()
obj.fit(data,"Z_Scratch")
standardize(obj)
obj.calInfo()

eff = obj.geteff()

print("initial eff=",eff)

for i in range(len(data.columns)-1,1,-1):
    
    obj = bc()
    obj.fit(data,"Z_Scratch")
    standardize(obj)
    obj.X_train,obj.X_test = PCAtransform(obj.X_train,obj.X_test,i)
    obj.calInfo()
    d.append(i)
    eff = obj.geteff()
    effs.append(eff)
    print(i,eff)
print("______________________________________________________")
print("dim= ",d[effs.index(max(effs))])
print("-------------------------------------------------------")
plt.plot(d,effs)
plt.show()
