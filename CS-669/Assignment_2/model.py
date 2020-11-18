import matplotlib.pyplot as plt
import numpy as np
import numba as nb
import time

@nb.njit
def set_mean(s):
    ans = 0
    for i in s:
        ans += i
    return ans/len(s)

class Point(np.ndarray):
    def __new__(self, *args, **kwargs):
        return super(Point, self).__new__(self, *args, **kwargs)
    def __array_finalize__(self, obj):
        self.cluster = -1

class Kmeans:
    def __init__(self, k, input_shape, distance_function=lambda x, y : np.linalg.norm(x-y)):
        # initializing centers using normal distribution
        self.centers = np.random.normal(0., 1., size=(k, input_shape)) 
        self.points = [ set() for i in range(k) ]
        self.distance_function = distance_function
        self.k = k
        self.input_shape = input_shape
    
    def fit(self, data, iterations=300):
        for point in data:
            distances = np.zeros(self.k, dtype=float)
            for i, center in enumerate(self.centers):
                distances[i] = self.distance_function(point, center)
            cluster_id = np.argmin(distances)
            self.points[cluster_id].add(point)
            
        del data

        for i in range(iterations):
            s_time = time.time()
            for cluster_id in range(self.k):
                self.resolve_cluster(cluster_id)
            e_time = time.time()
            print(f"Iteration {i+1} : {round(e_time-s_time, 2)}")
        

    def resolve_point(self, point: Point):
        distances = np.zeros(self.k, dtype=float)
        for i, center in enumerate(self.centers):
            distances[i] = self.distance_function(point, center)
        new_cluster = np.argmin(distances)
        if point.cluster == new_cluster:
            return
        if point.cluster != -1:
            self.points[point.cluster].remove(point)
        self.points[new_cluster].add(point)
        point.cluster = new_cluster

    def resolve_cluster(self, cluster_id : int):
        self.centers[cluster_id] = set_mean(self.points[cluster_id])
        for point in self.points[cluster_id]:
            distances = np.zeros(self.k, dtype=float)
            for i, center in enumerate(self.centers):
                distances[i] = self.distance_function(point, center)
            new_cluster = np.argmin(distances)
            if new_cluster == cluster_id:
                continue
            self.points[new_cluster].add(point)
            self.points[cluster_id].remove(point)
        self.centers[cluster_id] = set_mean(self.points[cluster_id])
        


    

        