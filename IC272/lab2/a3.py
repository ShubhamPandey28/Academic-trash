
import pandas as pd
import math
import matplotlib.pyplot as plt

data = pd.read_csv("winequality-red_miss.csv", sep=',')
data_copy = pd.read_csv("winequality-red_miss.csv", sep=',')
original_data = pd.read_csv("winequality-red_original.csv", sep=';')
cols = data.columns
size = len(data.values)
nan = float("NaN")
median = [0]*12
mean = [0]*12
mode = [0]*12
std_dev = [0]*12
new_median = [0]*12
new_mean = [0]*12
new_mode = [0]*12
new_std_dev = [0]*12

# Returns True if x is NaN else returns False
def isnan(x):
    if (x == "N/A" or x == "n/a" or x == "NA" or x == "na"):
        return True
    return x != x

def Compute_central():
    for i in range(len(cols)):
        median[i] = data[cols[i]].median()
        mean[i] = data[cols[i]].mean()
        mode[i] = list(data[cols[i]].mode())
        std_dev[i] = data[cols[i]].std()

def new_Compute_central():
    for i in range(len(cols)):
        new_median[i] = data_copy[cols[i]].median()
        new_mean[i] = data_copy[cols[i]].mean()
        new_mode[i] = list(map(float,(data_copy[cols[i]].mode())))
        new_std_dev[i] = data_copy[cols[i]].std()

def Replace_by_median():
    e = []
    for attribute in cols:
        Mean_Square = 0
        count = 0
        for i in range(len(data)):
            if (isnan(data[attribute][i])):
                data_copy[attribute][i] = round(data[attribute].median(), 4)
                count += 1
                Mean_Square += (data_copy[attribute][i] - original_data[attribute][i])**2
        Mean_Square /= count
        e.append(math.sqrt(Mean_Square))
    return e

def Replace_by_fillna():
    global data_copy
    e = []
    for attribute in cols:
        Mean_Square = 0
        count = 0
        for i in range(len(data)):
            if (isnan(data[attribute][i])):
                data_copy = data.fillna(method='ffill')
                count += 1
                Mean_Square += (data_copy[attribute][i] - original_data[attribute][i])**2
        Mean_Square /= count
        e.append(math.sqrt(Mean_Square))
    return e

def Replace_by_interpolate():
    global data_copy
    e = []
    for attribute in cols:
        Mean_Square = 0
        count = 0
        for i in range(len(data)):
            if (isnan(data[attribute][i])):
                data_copy = data.interpolate(method ='linear', limit_direction ='forward')
                count += 1
                Mean_Square += (data_copy[attribute][i] - original_data[attribute][i])**2
        Mean_Square /= count
        e.append(math.sqrt(Mean_Square))
    return e


Compute_central()
Error = Replace_by_interpolate()
new_Compute_central()

print("\nMean : \n",mean,"\n",new_mean)
print("\nMedian : \n",median,"\n",new_median)
print("\nMode : \n",mode,"\n",new_mode)
print("\nStandard Deviation : \n",std_dev,"\n",new_std_dev)
print("\n\nError : \n",Error)