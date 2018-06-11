import cv2
import numpy as np
import sys

img = cv2.imread('E:\\1.png')

#cv2.imshow('prot', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

img2, allcontours, hier = cv2.findContours(thr, cv2.RETR_LIST,
                                  cv2.CHAIN_APPROX_SIMPLE)
contours = list()
for c in allcontours:
    if len(c) > 10:
        contours.append(c)
contours = np.array(contours)
#print(type(contours))

for c in contours:
    eps = len(c) * 0.05
    a_c = cv2.approxPolyDP(c, eps, True)
    print(type(a_c))
    
    if not len(a_c) == 4:
        continue
    if not cv2.isContourConvex(a_c):
        continue
    minDist = sys.maxsize
    for i in range(0, 4):
        side = a_c[i] - a_c[(i+1)%4]
        print(side)
        squaLen = side[0].dot(side[0])
        minDist = min(minDist, squaLen)
    if minDist < 0.1:
        continue
    
    

cv2.drawContours(img,contours,-1,(255,0,0))

cv2.imshow('gray', img)

cv2.waitKey(0)
