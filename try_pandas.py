import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, read_csv

filename = 'C://Users//Apoorva//Desktop//A_Z Handwritten Data//A_Z Handwritten Data.csv'
chunksize =1
gaps = pd.read_csv(filename, chunksize=chunksize)
for chunk in gaps:
    print(gaps.head(2))
