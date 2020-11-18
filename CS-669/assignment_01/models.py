def getGaussian(x,mean,sig):
    return -(((x-mean)**2)/sig**2 + 2*log(sig))

class bayesClassifier:

    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.X = None
        self.Y = None
        self.infoMatrix = None
        self.fitted = False
        self.keys = None
        self.ce = False
        self.prior = None
    
    
    def fit(self,X, Y):
        self.X, self.Y = X, Y
        self.X_train, self.X_test, self.y_train, self.y_test = np.array(tts(X,Y,test_size=0.3, random_state=42))
        self.y_train = np.array(self.y_train)
        self.X_train = np.array(self.X_train)
        self.X_test = np.array(self.X_test)
        self.y_test = np.array(self.y_test)
        self.y_dim, self.prior = np.unique(self.y_train, return_counts=True)
        self.prior = self.prior / sum(self.prior)
        self.infoMatrix = np.empty((len(set(self.Y)),len(self.X[0]),2),dtype=float)         #[[[m11,sig11],[m12,sig12]],[[m21,sig21],[m22,sig22]]]
        
        self.fitted = True
        
        self.calInfo()
    
    
    def calInfo(self):
        if self.fitted:
            mp = {}
            
            for i in range(len(self.X_train)):
                try:
                    mp[self.y_train[i]].append(self.X_train[i])
                except:
                    mp[self.y_train[i]] = [self.X_train[i]]
            
            self.keys = list(mp.keys())

            self.info = {}

            for k in self.keys:
                self.info[k] = [np.mean(mp[k],axis=0),np.cov(np.array(mp[k]).T)]
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
    
    
    
    def predict(self,x):
        post = []
        for i in range(len(self.keys)):            
            l = mnorm.pdf(x,mean=self.info[self.keys[i]][0],cov=self.info[self.keys[i]][1], allow_singular=True)
            post.append(l*self.prior[self.keys[i]])
        label = np.argmax(post)
        confidence = post[label]
        return label, confidence
    
    def geteff(self):
        self.confMat = [ len(self.y_dim)*[0] for i in range(len(self.y_dim))]
        for i in range(len(self.X_test)):
            y_pred = self.predict(self.X_test[i])[0]
            self.confMat[y_pred][self.y_test[i]] += 1
                
        acc = 0
        for i in range(len(self.confMat)):
            acc += self.confMat[i][i]
        
        return acc/len(self.X_test) 
     
    