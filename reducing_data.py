#reducing database

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, read_csv

#filename = 'C://Users//Apoorva//Desktop//Book1.csv'
filename = 'C://Users//Apoorva//Desktop//A_Z Handwritten Data//A_Z Handwritten Data.csv'
chunksize =2
x= []
y= []
tf=0
listP = []
i=0
gaps = pd.read_csv(filename, chunksize=chunksize)

arr = []

for chunk in gaps:
    if(i%4 == 0):
        i = i + 1
        df = pd.DataFrame(chunk)
        for s in range(chunksize):
            x.append(df.iloc[s,0])
            listP = []
            for t in range(1,28):
                listP.append(df.iloc[s,t])
        y.append(listP)
    else:
            i = i + 1
            continue


a=np.array(x, 'int8')
b=np.array(y, 'float64')
'''len_x = len(x)
x.reshape(len_x,-1)
len_y = len(y)
y.reshape(len_y,-1)'''
print(a) #should be 1d
print(b)  #should be 2d



