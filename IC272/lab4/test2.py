import numpy as np
import matplotlib.pyplot as plt
from numpy import cov
import module2 as m2
from numpy.linalg import eig

from module2 import main

X=[]
Y=[]
for i in range(1000):
    x, y = np.random.multivariate_normal([0,0],[[7,10],[10,18]],1).T
    X=X+list(x)
    Y=Y+list(y)

data = m2.getData(X,Y)

lamdas, vectors = eig(V)
vecs=vectors.transpose()
print(vecs)
m2.plot(data,vecs)
plt.show()

main(X,Y)




