import cv2 as cv
import numpy as np

events = [i for  i  in dir(cv) if 'EVENT' in i]
print(events)


def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        #print(x + ', ' + y)
        mouse_pos = str(x) + ',' + str(y)
        scr_info = cv.putText(img, mouse_pos, (x, y), cv.FONT_HERSHEY_COMPLEX, 
                   1, (0, 255, 0), 1, cv.LINE_AA)
        
        cv.imshow("window", img)

img = cv.imread("my_image.jpg")
cv.imshow("window",img)

cv.setMouseCallback("window", click_event)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()