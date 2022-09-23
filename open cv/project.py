import cv2 as cv
import numpy as np


cap=cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow("Window", ret)



    if cv.waitKey(0) == ord('q'):
        break