import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.metrics import mean_squared_error
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.ar_model import AR

df = pd.read_csv("/home/dark_matter/Downloads/SoilForce.csv")
y_axis = df["Force"]
x_axis  = np.arange(1,142)
#plt.figure(figsize=(15,8)) magnify
plt.plot(x_axis,y_axis)
plt.xlabel("days")
plt.ylabel("Force")
plt.show()
x_ax = np.arange(1,71)

data = pd.DataFrame()
data['force(obs.)'] = df['Force'].iloc[1:]

data['force(t-1)'] = df['Force'].shift(1).iloc[1:]

corr_ = data.corr()
print("correlation matrix -- ")
print(corr_)

print(" autocorrelation plot-")
plot = plot_acf(df["Force"],lags=30)
plt.show()


X = data.values
train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

def model_persistence(x):
	return x
predictions = list()
for x in test_X:
	yhat = model_persistence(x)
	predictions.append(yhat)
test_score = np.sqrt(mean_squared_error(test_y, predictions))
print('Test RMSE: %.3f' % test_score)
plt.title("actual vs predicted")
plt.plot(x_ax,test_y)
plt.plot(x_ax,predictions)
plt.show()


autocorrelation_plot(df["Force"])
plt.show()



tr = df['Force'].head(70)
te = df['Force'].tail(70)
model = AR(tr)
model_fit = model.fit()
print('Lag(max. autocorrelation): %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)
predictions = model_fit.predict(start=len(tr), end=len(tr)+len(te)-1, dynamic=False)
#for i in range(len(predictions)):
    #print('predicted=%f, expected=%f' % (predictions[i+70], te[i+71]))
error = np.sqrt(mean_squared_error(te, predictions))
print('Test RMSE: %.3f' % error)
plt.plot(te)
plt.plot(predictions, color='red')
plt.show()