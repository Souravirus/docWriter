import matplotlib.pyplot as plt
import numpy
import pickle
from sklearn.externals import joblib
from PIL import Image
import cv2
from converter import imageprepare
from scipy import misc
from resizeimage import resizeimage

def cutImage(start, count, idx):
    img = misc.imread("Hello1.png")
    s1= img[:, start:count]
    img = Image.fromarray(s1)
    img.save("pic"+str(count)+".png") 
    mnist = imageprepare("pic"+str(count)+".png")
    mimage=[mnist[(i)*28:(i+1)*28] for i in range(28)]
    plt.subplot(3,3,idx+1)
    plt.imshow(mimage, cmap = plt.cm.gray_r, interpolation="nearest")
    cf = joblib.load("trainedCF.sav")
    print(cf.predict([mnist]), end = "")
    
A = cv2.imread("Hello1.png", 0)
cv2.imshow('image', A)
arr = numpy.asarray(A)
typearr = 0
start = 0
tCount = 0
mode = 0
breaking = 0
output = ""
for column in arr.T:
    count = 0
    prev = 1
    currmod = 0
    for i in column:
        if i!=255 and prev == 1:
            count += 1
            prev = 0
        elif i == 255:
            prev = 1
    if count == 0:
        currmod = 0
    else:
        currmod = 1
    if mode != currmod and mode == 1:
        cutImage(start, tCount, breaking)   
        start = tCount
        mode = currmod
        breaking+=1

    elif mode != currmod:
        mode = currmod
    tCount += 1
plt.show()
