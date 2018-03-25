import matplotlib.pyplot as plot
from sklearn import datasets
import numpy as np
from sklearn import svm
import pandas as pd
from pandas import DataFrame, read_csv

filename = 'C://Users//Apoorva//Desktop//A_Z Handwritten Data//A_Z Handwritten Data.csv'
chunksize =1
x= []
y= []
i=1
gaps = pd.read_csv(filename, chunksize=chunksize)
for chunk in gaps:
    i = i+1
    df = pd.DataFrame(chunk)
    for s in range(1):
        x.append(df.iloc[s,0])
        listP = []
        for t in range(1,28):
            listP.append(df.iloc[s,t])
        y.append(listP)
    if i>500000:
            break


#a = pd.DataFrame(x)
#b = pd.DataFrame(y)
a=np.array(x, 'int8')
b=np.array(y, 'float64')

print(a)
print(b)

digits = datasets.load_digits()
print((digits.data))  # learning data
clf = svm.SVC(gamma=0.001, C=100)
#print(type(digits.data))
# training
#x, y = digits.data[:-1], digits.target[:-1]
# tained upto -1....-1 for last element
#fit(data,target)
clf.fit(b, a)
my_data = b

#print('Prediction of last element:', clf.predict(digits.data[[-1]]))
print('Prediction of last element:', clf.predict(my_data))
print(my_data)
plot.imshow(digits.images[-1], cmap=plot.cm.gray_r, interpolation="nearest")
plot.show()
