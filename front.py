'''
Instruction:
press 3 to clear the number from display.
draw figure only in green grid by pressing the mouse button and dragging.
do not click outside the grid
'''
import pygame, time
import matplotlib.pyplot as plt
from sklearn.externals import joblib
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
BW = [black,white]
d7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,185,159,151,60,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,222,254,254,254,254,241,198,198,198,198,198,198,198,198,170,52,0,0,0,0,0,0,0,0,0,0,0,0,67,114,72,114,163,227,254,225,254,254,254,250,229,254,254,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,66,14,67,67,67,59,21,236,254,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,83,253,209,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,233,255,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,129,254,238,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,59,249,254,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,133,254,187,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,205,248,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,126,254,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,251,240,57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,221,254,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,203,254,219,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,38,254,254,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,224,254,115,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,133,254,254,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,242,254,254,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,254,254,219,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,254,207,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(d7)):
	d7[i]/=255
d7i = [d7[k*28:(k+1)*28] for k in range(28)]
#from pygame import *
pygame.init()
Total_Display = pygame.display.set_mode((600,600))
pygame.display.update()
sqs = 600//28
x,y = 0,0
td =  False
charMat = [[0]*28 for i in range(28)]
xo,yo = 0,0
Total_Display.fill(pink)
colr = white
#clf = joblib.load('clfjoblib.sav')
#clf is trained for 0-255 not 0-1
clf = joblib.load('trainedCF.sav')
#print(clf.predict([d7]))
#plt.imshow(d7i,cmap = plt.cm.gray_r, interpolation="nearest")
#print(dataset['image'][-2])
#plt.show()
#for zz in range(0,400):
zz = 0
while True:
	zz+=1
	for i in range(29):
		pygame.draw.line(Total_Display,(0,0,0),(i*15,0),(i*15,500))
		pygame.draw.line(Total_Display,(0,0,0),(0,i*15),(500,i*15))
	for i in range(21):
		pygame.draw.line(Total_Display,green,(i*15+15*4,15*4),(i*15+15*4,15*24))
		pygame.draw.line(Total_Display,green,(15*4,i*15+15*4),(15*24,i*15+15*4))
	time.sleep(.002)
	clock=pygame.time.Clock()
	clock.tick(100)
	ev = pygame.event.get()
	
	#print(event)
	
	#	pass
	for event in ev:
		if event.type == pygame.MOUSEMOTION:
			#print(pygame.mouse.get_pos())
			x,y =  event.pos
	for event in ev:
		if event.type == pygame.MOUSEBUTTONDOWN:
			td = True
		elif event.type == pygame.MOUSEBUTTONUP:
			td = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				colr = BW[0]
			elif event.key == pygame.K_1:
				colr = BW[1]
			elif event.key == pygame.K_3:
				Total_Display.fill(pink)
				charMat = [[0]*28 for i in range(28)]
			elif event.key == pygame.K_2:
				flat = []
				for exel in charMat:
					flat.extend(exel)
				print(len(flat))
				print(len(charMat))
				print(clf.predict([flat]))
	if td:
		if xo!=x-x%15 or yo!= y-y%15:
			#print(zz,'NRE')
			xo = x-x%15
			yo = y-y%15
			idxX = (xo+1)//15
			idxY = (yo+1)//15
			charMat[idxY][idxX] = 1*250
			
			charMat[idxY-1][idxX] = max(charMat[idxY-1][idxX],.7*250)
			charMat[idxY-1][idxX-1] = max(charMat[idxY-1][idxX-1],.7*250)
			charMat[idxY][idxX] = max(charMat[idxY][idxX],.7*250)
			charMat[idxY][idxX-1] = max(charMat[idxY][idxX-1],.7*250)
			#colr = BW[charMat[(xo+1)//15][(yo+1)//15]]
			pygame.draw.rect(Total_Display,colr,(x - x%15,y - y%15,15,15))
	if zz%100==0 and zz:
		flat = []
		for exel in charMat:
			flat.extend(exel)
		#print(len(flat))
		#print(len(charMat))
		print('Current figure',clf.predict([flat]))			
		#for e in charMat:
			#print(e)
		#print('Sllep')
		#time.sleep(10)
	#print(x,y,td)
	#if zz==399:
		#time.sleep(90)
	pygame.display.update()
