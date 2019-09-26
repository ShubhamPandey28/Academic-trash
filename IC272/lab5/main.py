from models import kNN, linear_regretion as lr
import preprocessor as p
import numpy as np

Xs, Ys = p.readCSV()

obj = kNN(3)
xn = list(p.normalize(Xs))

obj.fit(xn,Ys)
#obj.plotAcc(21)

xs = list(p.standardize(Xs))
obj.fit(xs,Ys)
#obj.plotAcc(21)

obj.fit(Xs,Ys)
#obj.plotAcc(21)

obj2 = lr(np.array(Xs),np.array(Ys))
print(obj2.geteff())