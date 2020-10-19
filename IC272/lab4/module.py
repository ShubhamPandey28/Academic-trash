import numpy as np
import matplotlib.pyplot as plt
from sys import getsizeof
import pandas as pd

class PCA(object):

    def __init__(self,dimension):
        self.dimension = dimension
        self.eigen_vectors = []
        self.eigen_pairs = []
        self.eigened = False
        self.data = None
        self.data_size = 0
        
    def construct_data(self,mean,cov,size):
        self.data = pd.DataFrame(np.random.multivariate_normal(mean=mean,cov=cov,size=size))
        self.data_size = getsizeof(self.data)
        self.cov = cov 

    def get_eigen_pairs(self):
        eig = np.linalg.eig(self.cov)
        self.eigen_vectors = eig[1]
        for i in range(len(eig[0])):
            self.eigen_pairs.append([eig[0][i],eig[1][i]])
        self.eigened = True

    def reduce_dimension_matrix(self,dimension):
        A = []
        if(not self.eigened):
            self.get_eigen_pairs()
        y = sorted(self.eigen_pairs,key = lambda x: abs(x[0]),reverse=True)
        for i in range(dimension):
            A.append(np.array(y[i][1]))
        A = np.array(A)
        return A

    def get_eigen_matrix(self):
        A = []
        if(not self.eigened):
            self.get_eigen_pairs()
        y = sorted(self.eigen_pairs,key = lambda x: abs(x[0]),reverse=True)
        for i in range(self.dimension):
            A.append(np.array(y[i][1]))
        A = np.array(A)
        return A

    def give_x(self,d_hat,A):
        data_hat = []
        for v in d_hat:
            v_hat = v[0]*A[0]
            for i in range(1,len(v)):
                v_hat += v[i]*A[i]
            data_hat.append(v_hat)
        data_hat = np.array(data_hat)
        return data_hat

    def get_reduced(self,dimension):
        A = self.reduce_dimension_matrix(dimension)
        d_hat = []
        for i in range(len(self.data)):
            v = np.array(self.data.iloc[[i]])
            d_hat.append(np.matmul(A,v.T))
        return self.give_x(d_hat,A)

    def get_reduced2(self):
        As = self.get_eigen_matrix()
        print(As)
        rlist = []
        for A in As:
            d_hat = []
            for i in range(len(self.data)):
                v = np.array(self.data.iloc[[i]])
                d_hat.append(np.matmul(A,v.T))
            rlist.append(self.give_x(d_hat,A))
        return rlist

    def plot_eigen_directed(self):
        if not self.eigened:
            self.get_eigen_pairs()
        xs = []
        data = self.get_reduced(1)
        for i in range(len(self.data)):
            xs.append(data[i][0])
        ys = []
        for i in range(len(self.data)):
            ys.append(data[i][1])
        
        plt.scatter(xs,ys)
        plt.quiver(self.eigen_vectors[0][0],self.eigen_vectors[0][1],scale=5,color='r')
        plt.quiver(self.eigen_vectors[1][0],self.eigen_vectors[1][1],scale=5,color='r')
        plt.show()

    def get_distance(self,v1,v2):
        dist = 0
        for i in range(len(v1)):
            dist += (v1[i]-v2[i])**2
        return dist

    def get_MSE(self,data_hat):
        mse = 0
        for i in range(len(self.data)):
            v = np.array(self.data.iloc[[i]][0])
            mse += self.get_distance(v,data_hat[i])
        return mse/len(self.data)

