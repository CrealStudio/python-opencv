import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


cap.set(3, 540)
cap.set(4, 540)

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    text = "width:" + str(cap.get(3)) +  " Height:" + str(cap.get(4))

    
    scr_info = cv.putText(frame, text, (100,450), cv.FONT_HERSHEY_COMPLEX, 
                   1, (0, 255, 0), 1, cv.LINE_AA)

    #frame = cv.flip(frame, 1)
    cv.imshow('camera', frame)

    if cv.waitKey(1) == ord('q'):
        break