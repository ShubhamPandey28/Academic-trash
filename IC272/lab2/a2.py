import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("winequality-red_miss-COPY.csv",sep=',')
cols = data.columns
size = len(data.values)
nan = float("NaN")
missing_per_tuple = [0]*len(cols)
missing_per_Column = [0]*len(cols)

# Returns True if x is NaN else returns False
def isnan(x):
    if (x == "N/A" or x == "n/a" or x == "NA" or x == "na"):
        return True
    return x != x

# Function that returns the number of NaN in all the attributes
def Count_Missing_inCol():
    global cols
    global missing_per_Column
    missing_per_Column = [0]*12
    for attribute in cols:
        column = data[attribute].values
        count = 0
        for i in column:
            if (isnan(i)):
                count += 1
        missing_per_Column.append(count)

# Function that returns the number of NaN in a particular Row/Tuple
def Count_Missing_inRow(row_number):
    count = 0
    tup = data.values[row_number]
    for i in tup:
        if (isnan(i)):
            count += 1
    return count

# Calculating Number of tuples missing 1 value, 2 values ...
def Print_missing_tuples():
    global size
    global missing_per_tuple
    missing_per_tuple = [0]*12
    for i in range(size):
        count  = Count_Missing_inRow(i)
        if (count != 0):
            missing_per_tuple[count-1] += 1
    print(missing_per_tuple)

# Drops Tuples missing Target Data Values
def Drop_by_target(target):
    global size
    for i in range (size,-1,-1):
        try:
            if ( isnan(data[target][i]) ):
                data.drop(i, inplace=True)
                size -= 1
        except  KeyError:
                pass

"""
# Plotting the above calculated data
x = range(1,len(cols)+1)
plt.plot(x,missing_per_tuple)
plt.xlabel("Number of Missing Values per tuples")
plt.ylabel("Number os tuples")
plt.show()
"""

print("Number of Tuples with more than 50% (6) of data missing ", sum(missing_per_tuple[5:]))
for i in range(size, -1, -1):
    try:
        count = Count_Missing_inRow(i)
        if (count >= 6):
            #print((data.values)[i])
            data.drop(i, inplace=True)
            size -= 1
    except IndexError:
        count = 0


Count_Missing_inCol()
print(missing_per_Column)
Print_missing_tuples()
Drop_by_target(cols[11])
Print_missing_tuples()
Count_Missing_inCol()
print(missing_per_Column)