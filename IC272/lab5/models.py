import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from sklearn.model_selection import train_test_split as tts


class kNN(object):

    def __init__(self,k):
        self.k = k
        self.train_data = None
        self.test_data = None
        self.target = None
        self.fitted = False
        self.ce = False
        self.eff = None
        self.confmat = []

    def fit(self,data,target):
        '''
            data: csv format,
            target_attribute: list of the attribute
        '''
        
        #self.train_data = [data[i] for i in range(k)]
        #self.test_data = [data[i] for i in range(k,len(data))]
        self.target = target
        #self.train_target = target[:k]
        #elf.test_target = target[k:]
        self.fitted = True
        self.train_data, self.test_data,self.train_target, self.test_target = tts(data,target,test_size=.3,random_state=42,shuffle=True)
    
    def getdistance(self,p1,p2):
        dist = 0
        for i in range(len(p1)):
            dist += (p1[i]-p2[i])**2
        return dist**0.5
    
    @classmethod
    def getmodeclass(self,l):
        s = set(l)
        clss = None
        mx = 0
        for el in s:
            tmp = l.count(el)
            if(tmp > mx):
                mx = tmp
                clss = el
        return clss

    def getclassof(self,test_point):   
        if(self.fitted):
            tup = [(self.getdistance(test_point,self.train_data[i]),self.train_target[i]) for i in range(len(self.train_data))]
            tup2 = sorted(tup,key = lambda x: x[0])
            
            l = []
            for i in range(self.k):
                l.append(tup2[i][1])
            return self.getmodeclass(l)

        else:
            print("You didn't fit any data to the model.")
            return

    def getefficiency(self):
        if(not self.ce):
            eff = 0
            fn=0
            tp=0
            tn=0
            fp=0
            for i in range(len(self.test_data)):
                clss = self.getclassof(self.test_data[i])
                if(int(self.test_target[i]) == 0 and int(clss) == 0):
                    eff += 1
                    tn += 1
                elif(int(self.test_target[i]) == 1 and int(clss)== 1):
                    eff += 1
                    tp += 1
                elif(int(self.test_target[i]) == 1 and int(clss) == 0):
                    fn += 1
                elif(int(self.test_target[i]) == 0 and int(clss) == 1):
                    fp += 1
            self.eff = [eff*100/len(self.test_data),[[tp,tn],[fp,fn]]]

        return self.eff
    
    def plotAcc(self,mxk):
        self.ce = False
        xs = []
        ys = []
        preff = 0
        for k in range(1,mxk,2):
            self.k = k
            eff = self.getefficiency()
            xs.append(k)
            ys.append(eff[0])
            preff = max(preff,eff[0])
            self.confmat.append(eff)
        self.maxeff = preff
        plt.plot(xs,ys)
        plt.show()
        plt.clf()



class linear_regretion(object):

    def __init__(self,data,target):

        self.train_data, self.test_data,self.train_target, self.test_target = tts(data,target,test_size=.3,random_state=42,shuffle=True)        
        self.w = linalg.solve(np.dot(self.train_data.T,self.train_data),np.dot(self.train_data.T,self.train_target))
        self.ce = False
        self.eff = 0

    def getans(self,i):
        p = np.dot(self.w,self.test_data[i])
        mx = max(self.train_target)
        mn = min(self.train_target)
        if p > mx:
            return mx
        if p < mn :
            return mn
        p1 = int(p)
        p2 = int(p)+1
        if abs(p2-p) > abs(p-p1):
            return p1
        return p2

    def geteff(self):
        if not self.ce:
            eff = 0
            for i in range(len(self.test_data)):
                if self.test_target[i] == self.getans(i):
                    eff += 1
            self.eff = eff*100/len(self.test_data)
        return self.eff
    
