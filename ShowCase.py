import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
import time

def CSVtoDict(filename,percentage):
	df = pd.read_csv(filename,header=None)
	rows,cols = df.shape
	rows = int(rows*percentage)
	dataset = {'data':[[0]*(cols-1) for r in range(rows)], 'target':[0]*rows }
	for r in range(rows):
		dataset['target'][r] = df[0][int(r/percentage)]
		for c in range(1,cols):
			dataset['data'][r][c-1] = df[c][int(r/percentage)]
	dataset['image'] = [[dataset['data'][r][(i)*28:(i+1)*28] for i in range(28)] for r in range(rows)]
	return dataset

sti = time.time()
cf = svm.SVC(gamma=0.000001,C=100)

filename = 'A_Z Handwritten Data.csv'
print('Started')
print(time.time()-sti)
dataset = CSVtoDict(filename,.01)
print('Loaded Dataset')
print(time.time()-sti)
dataset['target'] = [chr(i+65) for i in dataset['target']]
'''
filename = 'mnist_test.csv'
print('Loading',filename)
dataset2 = CSVtoDict(filename,1)
dataset['target'].extend(dataset2['target'][:])
dataset['image'].extend(dataset2['image'][:])
dataset['data'].extend(dataset2['data'][:])
print('Extended')
'''
print(time.time()-sti)
x = dataset['data'][:-3]
y = dataset['target'][:-3]
print('Training')
print(time.time()-sti)
cf.fit(x,y)
print('Saving...')
print(time.time()-sti)
filename = 'trainedCF.sav'
#joblib.dump(cf, filename)
print('Saved')
print(dataset.keys())
print(dataset['target'][-2],'Prediction',cf.predict([dataset['data'][-2]]))
print(time.time()-sti)
plt.imshow(dataset['image'][-2],cmap = plt.cm.gray_r, interpolation="nearest")
#print(dataset['image'][-2])
plt.show()
