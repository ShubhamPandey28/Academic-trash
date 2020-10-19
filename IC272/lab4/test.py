from module import PCA
import numpy as np
from sys import getsizeof as gso
import matplotlib.pyplot as plt

obj = PCA(2)

obj.construct_data([0,0],[[7,10],[10,18]],1000)
obj.get_eigen_pairs()
print(obj.data)
print(obj.eigen_pairs)
print(obj.reduce_dimension_matrix(1))
d = np.array(obj.data)

plt.scatter(d.T[0],d.T[1])
print("********")
d1 = obj.get_reduced(1)
print("evd")
d2 = obj.get_reduced2()
#print(d1[:10])
#print(d2)

obj.plot_eigen_directed()
