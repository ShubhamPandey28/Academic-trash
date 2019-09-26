from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



def standardize(object):
    scaler = StandardScaler()
    scaler.fit(object.X_train)
    object.X_train = scaler.transform(object.X_train)
    object.X_test = scaler.transform(object.X_test)

def PCAtransform(X_train,X_test,j):
    pca = PCA(n_components=j)
    pca.fit(X_train)
    return pca.transform(X_train),pca.transform(X_test)



    