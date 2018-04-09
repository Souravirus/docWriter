import numpy
import pyscreenshot as ImageGrab

def imageClick():
    im = ImageGrab.grab(bbox=(105, 170, 700, 365))
    im.show()
    im.save("Hello1.png")
    arr = numpy.asarray(im)
    print(arr)
    print(arr.shape)
