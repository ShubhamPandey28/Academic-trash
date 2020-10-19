import numpy as np
from math import log
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split as tts
from scipy.stats import multivariate_normal as mnorm
from sklearn.mixture import GaussianMixture as gm

def getGaussian(x,mean,sig):
    return -(((x-mean)**2)/sig**2 + 2*log(sig))

class bayesClassifier(object):

    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.X = None
        self.Y = None
        self.noatt = 0
        self.infoMatrix = None
        self.fitted = False
        self.keys = None
        self.ce = False
    
    
    def fit(self,dataframe,target_attribute):

        self.Y = dataframe[target_attribute]
        self.X = dataframe.drop(columns=[target_attribute])
        self.noatt = len(dataframe.columns) - 1

        self.X_train, self.X_test, self.y_train, self.y_test = np.array(tts(self.X,self.Y,test_size=0.3, random_state=42))
        self.y_train = np.array(self.y_train)
        self.X_train = np.array(self.X_train)
        self.X_test = np.array(self.X_test)
        self.y_test = np.array(self.y_test)

        self.infoMatrix = np.empty((len(set(self.Y)),len(self.X_train[0]),2),dtype=float)         #[[[m11,sig11],[m12,sig12]],[[m21,sig21],[m22,sig22]]]
        self.fitted = True

    
    
    def calInfo(self):
        if self.fitted:
            self.class_mp = {}
            
            for i in range(len(self.X_train)):
                try:
                    self.class_mp[self.y_train[i]].append(self.X_train[i])
                except:
                    self.class_mp[self.y_train[i]] = [self.X_train[i]]
            
            self.keys = list(self.class_mp.keys())

            self.info = {}

            for k in self.keys:
                self.info[k] = [np.mean(self.class_mp[k],axis=0),np.cov(np.array(self.class_mp[k]).T)]
            '''
            for j in range(len(self.keys)):
                l = np.mean(mp[self.keys[j]],axis=0)
                l2 = np.std(mp[self.keys[j]],axis=0)
                for i in range(len(self.X_train[0])):
                    self.infoMatrix[j][i][0] = l[i]
                    self.infoMatrix[j][i][1] = l2[i]
            '''
        else:
            raise Exception("Please fit the data into the model first.")
    
    def set_GMM_model(self,q):
        self.q = q
        self.GM_mdl = []
        for i in range(len(self.keys)):
            mdl = gm(q,covariance_type='diag')
            mdl.fit(self.class_mp[self.keys[i]])
            self.GM_mdl.append(mdl)
    
    def predict(self,x):
        lhds = []
        for i in range(len(self.keys)):            
            l = mnorm.pdf(x,mean=self.info[self.keys[i]][0],cov=self.info[self.keys[i]][1], allow_singular=True)
            lhds.append(l)
        mx = lhds.index(max(lhds))
        return self.keys[mx]

    def predictnew(self,x):
        lhds = []
        for i in range(len(self.keys)):            
            #l = mnorm.pdf(x,mean=self.info[self.keys[i]][0],cov=self.info[self.keys[i]][1], allow_singular=True)
            l = self.GM_mdl[i].score_samples([x])
            lhds.append(l)
        mx = lhds.index(max(lhds))
        return self.keys[mx]
    
    def geteff(self):
        self.confMat = [[0,0],[0,0]]
        for i in range(len(self.X_test)):
            self.confMat[self.predictnew(self.X_test[i])][self.y_test[i]] += 1

        self.eff = (self.confMat[0][0] + self.confMat[1][1])*100/len(self.X_test)

        return self.eff

