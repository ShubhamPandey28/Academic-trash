import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import metrics

data = pd.read_csv("data.csv")
Y = np.array(data["Species"])
data.drop(columns=["Species"],inplace=True)
pca = PCA(n_components=2)

pca.fit(np.array(data))
X = pca.transform(data)

model = GaussianMixture(n_components=3)
model.fit(X)
y_pred = model.predict(X)
contingency_matrix = metrics.cluster.contingency_matrix(Y, y_pred)
print(contingency_matrix)
print("PURITY SCORE =",np.sum(np.amax(contingency_matrix,axis=0))/np.sum(contingency_matrix))

#plotting
colors = ["red","blue","green"]
for i in range(len(X)):
    plt.scatter(X[i][0],X[i][1],color=colors[y_pred[i]])
plt.show()

dist = []
pss = []
ks = list(range(2,8))
for k in range(2,8):
    model = GaussianMixture(n_components=k)
    model.fit(X)
    dist.append(model.score(X))
    y_pred = model.predict(X)
    cm = metrics.cluster.contingency_matrix(Y, y_pred)
    ps = np.sum(np.amax(cm,axis=0))/np.sum(cm)
    pss.append(ps)
plt.plot(ks,pss)
plt.show()

plt.plot(ks,dist)
plt.show()