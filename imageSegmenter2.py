import matplotlib.pyplot as plt
import numpy
from PIL import Image
import cv2
from converter import imageprepare
from scipy import misc
from resizeimage import resizeimage

def cutImage(start, count):
    img = misc.imread("Hello1.png")
    print(img.shape)
    s1= img[:, start:count]
    img = Image.fromarray(s1)
    img.save("pic"+str(count)+".png")
    mnist = imageprepare("pic"+str(count)+".png")
    
     

A = cv2.imread("Hello1.png", 0)
cv2.imshow('image', A)
arr = numpy.asarray(A)
print(arr)
print(arr.shape)
typearr = 0
start = 0
tCount = 0
mode = 0
breaking = 0
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
        print("start")
        print(start)
        print("tCount")
        print(tCount)
        cutImage(start, tCount)   
        start = tCount
        mode = currmod
        print("mod changed to")
        print(mode)
        breaking+=1
    elif mode != currmod:
        mode = currmod
    print(count)
    tCount += 1
print("breaking")
print(breaking)
