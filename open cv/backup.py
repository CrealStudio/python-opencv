import cv2 as cv
import numpy as np

#cap = cv.VideoCapture(0)

#cap.set(3, 540)
#cap.set(4, 540)

img = cv.imread("open cv/chess.png")
img = cv.resize(img, (0,0), fx=0.3, fy=0.3)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x,y), 5, (0,0, 255), -1)

cv.imshow("WINDOW", img)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()
