import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")
col=data.columns
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=42,shuffle=True)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
red=[]
knnacc=[]
bayacc=[]
for j in range(1,len(col)):
    pca = PCA(n_components=j)
    red.append(j)
    pca.fit(X_train)
    x_pca_train = pca.transform(X_train)
    x_pca_test = pca.transform(X_test)
    a=[]
    b=[]
    c=[]
    d=[]
    print("___________________________")
    print("dim =",j)
    print("  ")
    for i in range(1,22,2):
        classifier = KNeighborsClassifier(n_neighbors=i)
        classifier.fit(x_pca_train, y_train)
        y_pred = classifier.predict(x_pca_test)
        c.append(confusion_matrix(y_test, y_pred))
        a.append(accuracy_score(y_test, y_pred))
        b.append(i)
        d.append([accuracy_score(y_test, y_pred),i])
    print("k=",max(d)[1],", Acc=",max(d)[0])
    
    classifier = GaussianNB()
    classifier.fit(x_pca_train, y_train)
    y_pred = classifier.predict(x_pca_test)
    cm = confusion_matrix(y_test, y_pred)
    print("conf Matrix:",cm)
    print("Acc of bayess classifier:-",accuracy_score(y_test, y_pred))
    print("___________________________")
    
    knnacc.append(max(d)[0])
    bayacc.append(accuracy_score(y_test, y_pred))

print("___________________________")
plt.plot(red,knnacc)
plt.title("KNN acc. vs dimension")
plt.ylim((0,1))
plt.xlabel("dimension")
plt.ylabel("accuracy")
plt.show()
print("Max kNN Acc=",max(knnacc),"at dimesion =",red[knnacc.index(max(knnacc))])
print("___________________________")
plt.title("Bayes acc vs dimension")
plt.plot(red,bayacc)
plt.ylim((0,1))
plt.xlabel("dimension")
plt.ylabel("accuracy")
plt.show()

print("Max Bayes Acc=",max(bayacc),"at dimesion =",red[bayacc.index(max(bayacc))])
print("___________________________")