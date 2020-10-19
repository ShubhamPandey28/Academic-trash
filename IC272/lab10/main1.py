from sklearn.cluster import KMeans
from sklearn.metrics import homogeneity_score as hs

pts = []
with open("data.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        x,y = map(float,line.split(" "))
        pts.append([x,y])

model = KMeans(n_clusters=4)
model.fit(pts)
centroids = model.cluster_centers_
labels = model.labels_
print("Sum of squared distance =",model.inertia_)

