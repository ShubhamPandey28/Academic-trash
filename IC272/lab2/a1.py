import pandas as pd

data = pd.read_csv("winequality-red_miss-COPY.csv",sep=',')
cols = data.columns
nan = float("NaN")

# Returns True if x is NaN else returns False
def isnan(x):
    if (x == "N/A" or x == "n/a" or x == "NA" or x == "na"):
        return True
    return x != x

# Function that returns the number of NaN in a particular attribute
def Count_Missing(attribute):
    column = data[attribute].values
    count = 0
    for i in column:
        if (isnan(i)):
            count += 1
    return count

def Print_total():
    total = 0
    for i in cols:
        x = Count_Missing(i)
        total += x
        print(i,x)
    print("Total : ",total)

def Delete_data(num , attribute):
    for i in range(len(data)):
        if ( isnan(data[attribute][i]) == False ):
            data[attribute][i] = "N/A"
            num -= 1
        if (num == 0) :
            break

def Replace_missing_data(num , attribute):
    for i in range(len(data)):
        if (isnan(data[attribute][i])):
            data[attribute][i] = round(data[attribute].mean(), 2)
            num -= 1
        if (num == 0) :
            break

Print_total()
Delete_data(2, "fixed acidity")
Print_total()