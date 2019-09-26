from models import bayesClassifier as bc
import pandas as pd
data = pd.read_csv("data.csv")
obj = bc()
obj.fit(data,"class")
obj.calInfo()
print(obj.predict(obj.X_test[0]),obj.y_test[0])