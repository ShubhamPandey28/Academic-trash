from sklearn.mixture import GaussianMixture
from sklearn import model_selection
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def train_test_split(data,test_size,seed): 
    return model_selection.train_test_split(data.iloc[:,0:-1],data.iloc[:,-1],test_size=test_size,random_state=seed) 
def standardisation(dataframe): 
    return StandardScaler().fit_transform(dataframe.values)
def stdatts(dataframe): 
    dataframe.iloc[:,0:-1] = standardisation(dataframe.iloc[:,0:-1])
def makegmm(c1,c2,q): 
    return GaussianMixture(n_components=q).fit(c1),GaussianMixture(n_components=q).fit(c2)
def classifieddata(data_train,c1,c2): 
    return data_train[data_train["Z_Scratch"]==c1].iloc[:,0:-1],data_train[data_train["Z_Scratch"]==c2].iloc[:,0:-1]
