import models
from models import kNN
import preprocessor as p

filePath = "data.csv"
Xs = []
Ys = []
with open(filePath,'r') as f:
    lines = f.readlines()

    for line in lines[1:]:
        l = list(map(float,line[:-1].split(",")))
        Xs.append(l[:-1])
        Ys.append(l[-1])


obj = kNN(3)
xn = list(p.normalize(Xs))

obj.fit(xn,Ys)
obj.plotAcc(10)

xs = list(p.standardize(Xs))
obj.fit(xs,Ys)
obj.plotAcc(50)