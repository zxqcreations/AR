import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    if not cap.isOpened():
        print('camera cannot work properly, please check it.')
        break

    ret, img = cap.read()

    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    img2, allcontours, hier = cv2.findContours(thr, cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_SIMPLE)
    contours = list()
    for c in allcontours:
        if len(c) > 50:
            contours.append(c)
    contours = np.array(contours)
    #print(type(contours))
    
    cv2.drawContours(img,contours,-1,(255,0,0))
    
    cv2.imshow('gray', img)

    if cv2.waitKey(20) > 0:
        break

cap.release()
cv2.destroyAllWindows()
