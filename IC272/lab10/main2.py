from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import homogeneity_score as hs
from sklearn import metrics

data = pd.read_csv("data.csv")
Y = np.array(data["Species"])
data.drop(columns=["Species"],inplace=True)
pca = PCA(n_components=2)

pca.fit(np.array(data))
x = pca.transform(data)

model = KMeans(n_clusters=3)
model.fit(x)
true = Y

contingency_matrix = metrics.cluster.contingency_matrix(true, model.labels_)
print(contingency_matrix)
print("PURITY SCORE =",np.sum(np.amax(contingency_matrix,axis=0))/np.sum(contingency_matrix))

colors = ["red","blue","green"]
for i in range(len(x)):
    plt.scatter(x[i][0],x[i][1],color=colors[model.labels_[i]])
plt.show()


dist = []
ks = list(range(2,8))
for k in range(2,8):
    model = KMeans(n_clusters=k)
    model.fit(x)
    dist.append(model.inertia_/len(x))

plt.plot(ks,dist)
plt.show()

print("EM K =",4)