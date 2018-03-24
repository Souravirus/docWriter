import pyscreenshot as ImageGrab

def imageClick():
    im = ImageGrab.grab(bbox=(100, 180, 700, 375))
    im.show()
    im.save("Hello1.png")
