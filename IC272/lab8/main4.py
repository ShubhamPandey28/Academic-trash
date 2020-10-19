import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures 
import scipy.stats as st
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

dataset = pd.read_csv("data.csv")
feature = 'pressure'
label = 'temperature'
dataset.plot(x='pressure', y='temperature', style='o')  
plt.title("press vs temp")  
plt.xlabel("press")  
plt.ylabel("temp")  
plt.show()


X = dataset['pressure'].values.reshape(-1,1)

y = dataset['temperature'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
print("intercept=",regressor.intercept_)
print("coef. of line",regressor.coef_)
y_pred = regressor.predict(X_test)
x_pred = regressor.predict(X_train)
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

plt.scatter(X_test, y_test,  color='black')
plt.xlabel('press.')
plt.ylabel('temp')
plt.title('degree=1 ')
plt.plot(X_test, y_pred, color='yellow', linewidth=2)
plt.show()

print('RMSE test: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
# if rmse for train data becomes 0, means over-fit.
print('RMSE train:', np.sqrt(metrics.mean_squared_error(y_train, x_pred)))

plt.title(" act vs pred temp")
plt.xlabel("act")
plt.ylabel("pred")
plt.scatter(y_test,y_pred)
plt.show()


X = dataset['pressure'].values.reshape(-1,1)

y = dataset['temperature'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rmse_te=[]
rmse_tr=[]
x_axis = np.arange(2,6)
for i in range(2,6):
    model = PolynomialFeatures(degree = i)
    X_ = model.fit_transform(X_train)
    X_ = pd.DataFrame(X_)
    
    X_test_ = model.fit_transform(X_test)
    X_test_ = pd.DataFrame(X_test_)
   
    regressor = LinearRegression() 
    regressor.fit(X_, y_train)
    y_pred = regressor.predict(X_test_)
    x_pred = regressor.predict(X_)
    rmse_test=np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    rmse_te.append(rmse_test)
    rmse_train=np.sqrt(metrics.mean_squared_error(y_train, x_pred))
    rmse_tr.append(rmse_train)
    print("for degree",i)
    print('Root Mean Squared Error (for test data):',rmse_test)
    print('Root Mean Squared Error (for training data):',rmse_train)
    
    plt.scatter(X_train, y_train,  color='black')
    
    plt.xlabel('press')
    plt.ylabel('temp')
    plt.scatter(X_train, x_pred, color='red', linewidth=2)
    
    plt.show()
    plt.title("act temp vs ped temp")
    plt.xlabel("act temp")
    plt.ylabel("pred temp")
    plt.scatter(y_test,y_pred)
    plt.axis('equal')
    plt.show()
plt.bar(x_axis,rmse_tr)
plt.xlabel('degree', fontsize=15)
plt.ylabel('RMSE', fontsize=15)
plt.xticks(x_axis, fontsize=15, rotation=30)
plt.show()
    
plt.bar(x_axis,rmse_te)
plt.xlabel('Degree', fontsize=15)
plt.ylabel('Rmse value', fontsize=15)
plt.xticks(x_axis, fontsize=15, rotation=10)
plt.show()    
    
X = dataset[['humidity', 'pressure', 'rain', 'lightAvg', 'lightMax', 'moisture']]
y = dataset['temperature']

pearson = []
for i in range(len(X.columns)):
    pearson.append([st.pearsonr(X.iloc[:,i],y)[0],X.columns[i]])
pearson.sort(reverse=True)
X=dataset[[pearson[0][1],pearson[1][1]]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
inter = regressor.intercept_ 

y_pred = regressor.predict(X_test)
x_pred = regressor.predict(X_train)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print('RMSE test:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('RMSE train:', np.sqrt(metrics.mean_squared_error(y_train, x_pred)))

cq=list(coeff_df['Coefficient'])
c1 = cq[0]
c2 = cq[1]

print("humidity and lightAvg")

def f(x,y):
    return np.array(c1*x+c2*y+inter)

x_axis = np.linspace(30,100,945)
y_ax = np.linspace(-1,101,945)

X_axis,y_axis = np.meshgrid(x_axis,y_ax)
Z = f(X_axis,y_axis)
ax=Axes3D(plt.figure())
ax.plot_surface(X_axis,y_axis,Z)
plt.xlabel("humidity")
plt.ylabel("lightAvg")
plt.show()

plt.title("act vs pred")
plt.xlabel("act")
plt.ylabel("pred")
plt.scatter(y_test,y_pred)
plt.show()


for i in range(2,6):
    model = PolynomialFeatures(degree = i)
    X_ = model.fit_transform(X_train)
    X_ = pd.DataFrame(X_)
    X_test_ = model.fit_transform(X_test)
    X_test_ = pd.DataFrame(X_test_)
    regressor = LinearRegression() 
    regressor.fit(X_, y_train)
    y_pred = regressor.predict(X_test_)
    x_pred = regressor.predict(X_)
    rmse_test=np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    rmse_train=np.sqrt(metrics.mean_squared_error(y_train, x_pred))
    print("degree=",i)
    print('RMSE test=',rmse_test)
    print('RMSE train=',rmse_train)
    plt.title(" act vs pred deg="+str(i))
    plt.xlabel("act")
    plt.ylabel("pred")
    plt.scatter(y_test,y_pred)
    plt.axis('equal')
    plt.show()
