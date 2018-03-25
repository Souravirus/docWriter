import numpy
import pyscreenshot as ImageGrab

def imageClick():
    im = ImageGrab.grab(bbox=(105, 180, 700, 375))
    im.show()
    im.save("Hello1.png")
    arr = numpy.asarray(im)
    print(arr)
    print(arr.shape)
