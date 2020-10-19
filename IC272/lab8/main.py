import pandas as pd
import numpy as np
from model import extractAttribute, linear_regretion, insert, polynomialRegression as lr2
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

X, Y = extractAttribute(data,["pH"],"quality")
Xcpy = insert(X)
lr = linear_regretion()
lr.fit(Xcpy,Y)
print("Linear p=1",lr.get_RMSE())
print("W=",lr.w)

lrp = lr2()
rmses = []
ps = [2,3,4,5]
for p in ps:
    lrp.fit(X,Y,p)
    # x1,y1,x2,y2 = min(X),lrp.predict([1,min(X)]),max(X),lrp.predict([1,max(X)])
    plt.scatter(X,Y)
    # plt.plot([x1,x2],[y1,y2],color="black")
    # plt.show()
    rmse = lrp.get_RMSE()
    rmses.append(rmse)
    print("degree= "+str(p)+": ",rmse)
    lrp.plot2D()
    plt.plot(lrp.y_test,lrp.y_obs)
    plt.show()
plt.plot(ps,rmses)
plt.show()

