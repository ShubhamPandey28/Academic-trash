from model import data_analysis_model as DAM
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

mdl = DAM(data)

mdl.min_max_normalization(0,2,"pH")

print(max(mdl.dataframe["pH"]))