import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn import model_selection
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from func import *

data = pd.read_csv("data.csv")
stdatts(data)

q_values = [2,4,8,16]

X_train, X_test, Y_train, Y_test = train_test_split(data,0.3,42)
X_train0,X_train1=classifieddata(pd.concat([X_train,Y_train],axis=1),0,1)
print("Original data:")
for q in q_values:
    gmm0,gmm1 = makegmm(X_train0,X_train1,q)
    
    Y_pred=[int(gmm0.score_samples(X_test)[i]<gmm1.score_samples(X_test)[i]) for i in range(len(X_test))]
    
    print([list(confusion_matrix(Y_test,Y_pred)[i]) for i in range(len(confusion_matrix(Y_test,Y_pred)))],'\t',accuracy_score(Y_test,Y_pred))


for i in range(1,len(list(data))):
    pca = PCA(n_components=i)
    
    reduced_data = pd.concat([pd.DataFrame(data = pca.fit_transform(data.copy().iloc[:,0:-1]),columns=['comp '+str(n) for n in range(i)]),data.copy().iloc[:,-1]], axis = 1)
    
    X_train, X_test, Y_train, Y_test = train_test_split(reduced_data,0.3,42)
    X_train0,X_train1=classifieddata(pd.concat([X_train,Y_train],axis=1),0,1)
    
    print("\ndim = "+str(i))
    for q in q_values:
        gmm0,gmm1 = makegmm(X_train0,X_train1,q)
        
        Y_pred=[int(gmm0.score_samples(X_test)[i]<gmm1.score_samples(X_test)[i]) for i in range(len(X_test))]
        
        print([list(confusion_matrix(Y_test,Y_pred)[i]) for i in range(len(confusion_matrix(Y_test,Y_pred)))],'\t',accuracy_score(Y_test,Y_pred))