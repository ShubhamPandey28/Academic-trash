import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
data = pd.read_csv("data.csv")

X = data["Date"]
Y = data["Force"]
X = list(X)
Y = list(Y)

plot_acf(Y,lags=35)
plt.show()

plt.ylabel("Force")
plt.xlabel("Date")
plt.plot(X,Y)
plt.show()