import numpy as np
import sklearn.preprocessing as sp

def normalize(l):
    return sp.normalize(np.array(l))
    

def standardize(l):
    l = np.array(l)
    return sp.normalize(l,axis=1,norm="l1")