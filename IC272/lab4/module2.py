from numpy.linalg import eig
from numpy import cov
import numpy as np
import matplotlib.pyplot as plt



X=[]
Y=[]
for i in range(1000):
    x, y = np.random.multivariate_normal([0,0],[[7,10],[10,18]],1).T
    X=X+list(x)
    Y=Y+list(y)

def getData(X,Y):
    C=[]
    for i in range(len(X)):
        C.append([X[i],Y[i]])
    C=np.array(C)
    return C

def plot(C,vecs):
    plt.scatter(C.T[0],C.T[1],marker='x')
    plt.quiver(vecs[0][0],vecs[0][1],scale=5,color='r')
    plt.quiver(vecs[1][0],vecs[1][1],scale=5,color='r')

def main(X,Y):
    C=[]
    for i in range(len(X)):
        C.append([X[i],Y[i]])
    C=np.array(C)

    plt.scatter(C.T[0],C.T[1],marker='x')

    V = cov(C.T)

    
    lamdas, vectors = eig(V)
    vecs=vectors.transpose()
    plt.quiver(vecs[0][0],vecs[0][1],scale=5,color='r')
    plt.quiver(vecs[1][0],vecs[1][1],scale=5,color='r')

    P = vectors.T.dot(C.T)    
    D1=vectors.T[0].dot(C.T)   
    D2=vectors.T[1].dot(C.T)   

    D0p=[]     
    D1p=[]      
    D2p=[]     
    for i in range(1000):
        D1p.append(D1[i]*vectors.T[0])
        D2p.append(D2[i]*vectors.T[1])
        D0p.append(np.add(P.T[i][0]*vectors.T[0],P.T[i][1]*vectors.T[1]))

    D1p=np.array(D1p).transpose()
    D2p=np.array(D2p).transpose()


    plt.scatter(D1p[0],D1p[1],marker='x')    
    plt.scatter(D2p[0],D2p[1],marker='x')    


    plt.xlim([-25,20])
    plt.ylim([-15,15])

    E1=[]
    E2=[]
    E0=[]

    for i in range(1000):
        e0=((C[i][0]-D0p[i][0])**2+(C[i][1]-D0p[i][1])**2)
        e1=((C[i][0]-D1p.T[i][0])**2+(C[i][1]-D1p.T[i][1])**2)
        e2=((C[i][0]-D2p.T[i][0])**2+(C[i][1]-D2p.T[i][1])**2)
        E0.append(e0)
        E1.append(e1)
        E2.append(e2)

    error0=(sum(E0)**0.5)/len(E0) 
    error1=(sum(E1)**0.5)/len(E1) 
    error2=(sum(E2)**0.5)/len(E2) 


