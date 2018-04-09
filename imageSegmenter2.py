import matplotlib.pyplot as plt
import numpy,time
import pickle
from sklearn.externals import joblib
from PIL import Image
import cv2
from converter import imageprepare
from scipy import misc
from resizeimage import resizeimage
#from draw import Paint
def cutImage(start, count, mini, maxi, idx):
    print("Loaded f")
    img = misc.imread("Hello1.png")
    s1= img[mini:maxi, start:count]
    img = Image.fromarray(s1)
    img.save("pic"+str(count)+".png") 
    mnist = imageprepare("pic"+str(count)+".png")
    mimage=[mnist[(i)*28:(i+1)*28] for i in range(28)]
    plt.subplot(3,3,idx+1)
    print("Loaded Subplot")
    plt.imshow(mimage, cmap = plt.cm.gray_r, interpolation="nearest")
    cf = joblib.load("trainedCF.sav")
    cf2 = pickle.load(open('clfver2.5Both1000P.sav','rb'))
    cf3 = pickle.load(open('clfvM2.6v10e7BothAllkaliP.sav','rb'))    
    print('Prediction',cf.predict([mnist]),cf2.predict([mnist]),cf2.predict([mnist]))
    return cf2.predict([mnist])

#Paint()
def getText():
	A = cv2.imread("Hello1.png", 0)
	#print("Loaded")
	#cv2.imshow('image', A)
	arr = numpy.asarray(A)
	#print("Loaded")
	typearr = 0
	start = 0
	tCount = 0
	mode = 0
	breaking = 0
	output = ""
	mini = 0
	maxi = 0
	#print("Loaded")
	OutputStr = ''
	for column in arr.T:
		count = 0
		#print("Loaded T")
		prev = 1
		currmod = 0
		n = 0
		for i in column:
			
			if i!=255 and prev == 1:
				count += 1
				prev = 0
				if mini == 0:
					mini = n
				elif n < mini:
					mini = n
			elif i == 255 and prev == 0:
				prev = 1
				if maxi == 0:
					maxi = n
				elif n > maxi:
					maxi =n
			n+=1
		#print("Loaded G",count,currmod,mode)
		
		if count == 0:
			currmod = 0
		else:
			currmod = 1
		if mode != currmod and mode == 0:
			start = tCount
			mode = currmod
		elif mode != currmod and mode == 1:
			#print("Loaded 4")
			OutputStr+=cutImage(start, tCount, mini, maxi, breaking)[0]   
			start = tCount
			mode = currmod
			maxi = 0
			mini = 0
			breaking+=1

		tCount += 1
	#time.sleep(3)
	print(OutputStr)
	#plt.show()
	return OutputStr
if __name__=='__main__':
	getText()
