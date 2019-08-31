import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("winequality-red_miss.csv")
global data
def isnan(x):
    if x in ["na","NA","N/A","n/a"]:
        return True
    return False

def find_missing_value_in_attribute(attribute):
    global data
    count=0
    for i in range(len(data)):
        if(isnan(data[attribute][i])):
            count+=1
    return count

def replace_value():
    global data
    count1=0
    count2=0
    for i in range(len(data)):
        if(not isnan(data["fixed acidity"][i])):
            count2+=1
            data["fixed acidity"][i]="N/A"
        if(count2 >=2):
            break

    for i in range(len(data)):
        if(not isnan(data["volatile acidity"][i])):
            count1+=1
            data["volatile acidity"][i]="n/a"
        elif(count1 >=2):
            break
    print(find_missing_value_in_attribute("volatile acidity"))    


