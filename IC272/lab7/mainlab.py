from model import *
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")



for q in [2,4,8,16]:
    classifier = bayesClassifier()

    classifier.fit(data,"Z_Scratch")

    classifier.calInfo()
    classifier.set_GMM_model(q)

    classifier.geteff()

    print(classifier.eff)




