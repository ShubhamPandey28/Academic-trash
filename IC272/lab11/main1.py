import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,AgglomerativeClustering,DBSCAN
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn import metrics
from scipy.optimize import linear_sum_assignment


def purity_score(y_true, y_pred):
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    row_ind, col_ind = linear_sum_assignment(-contingency_matrix)
    return contingency_matrix[row_ind, col_ind].sum() / np.sum(contingency_matrix)
'''
digits = load_digits()
datax=digits.data
datay=digits.target
'''

dataD = pd.read_csv("data.csv")
datay = np.array(dataD["Species"])
datax = np.array(dataD.drop(columns=["Species"]))

data = PCA(n_components=2).fit_transform(datax)
data=pd.DataFrame(data)

plt.scatter(data.iloc[:,0],data.iloc[:,1],color="blue")
plt.show()


Kmean = KMeans(n_clusters=3)
Kmean.fit(data)
labels = Kmean.predict(data)

print("---KMeans---")

plt.scatter(data.iloc[:,0],data.iloc[:,1],c=labels,cmap='viridis')
centers=Kmean.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],s=100,c='black')
plt.show()
print("purity score =",purity_score(pd.DataFrame(datay),pd.DataFrame(labels)))
print()

print("---Agglomerative Clustering---")
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='average')
labelag=cluster.fit_predict(data)
plt.scatter(data.iloc[:,0],data.iloc[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()
print("purityScore = ",purity_score(pd.DataFrame(datay),pd.DataFrame(labelag)))
print()

print("---DBSCAN---")
epsp=[0.05,0.5,0.95]
min_samplesp=[1,10,30,50]
ps=[]
arr = []
for i in epsp:
    for j in min_samplesp:
        db = DBSCAN(eps = i, min_samples = j).fit(data) 
        labels1 = db.fit_predict(data)
        arr.append([i,j])
        ps.append(purity_score(pd.DataFrame(datay),pd.DataFrame(labels1)))
psmax = max(ps)
ind = ps.index(psmax)
eps = arr[ind][0]
min_samples = arr[ind][1]
print("eps=",eps,"min_samples=",min_samples)
db = DBSCAN(eps = eps, min_samples =min_samples).fit(data) 
labels1 = db.labels_
plt.scatter(data.iloc[:,0],data.iloc[:,1], c=db.labels_, cmap='rainbow')
plt.show()
print("purityScore =",purity_score(pd.DataFrame(datay),pd.DataFrame(labels1)))
