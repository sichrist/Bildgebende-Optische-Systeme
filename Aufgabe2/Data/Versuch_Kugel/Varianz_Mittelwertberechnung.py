#Kugelversuch

import cv2
import numpy as np

#d1=input('Bildpfad_Dunke_1')
#d2=input('Bildpfad_Dunkel_2')
h1=input('Bildpfad_Hell_1')
h2=input('Bildpfad_Hell_2')
#img1=cv2.imread(d1)
#img2=cv2.imread(d2)
img3=cv2.imread(h1)
img4=cv2.imread(h2)
#imgMd=(img1+img2)/2
imgMh=(img3+img4)/2

#imgM=(imgMd+imgMh)/2
imgMh = imgMh[:,:,0]
print(imgMh.shape)
uY=imgMh.mean()
var=imgMh.var()
std=imgMh.std()
print('DN:',uY)
print('Varianz:',var)
print('Std:',std)
