import cv2
import numpy as np

img = cv2.imread('hospital2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 10, 0.05, 0.25)
corners = np.float32(corners)

for item in corners:
    x,y = item[0]
    cv2.circle(img, (x,y), 4, 255, -1)

cv2.imshow("Cantos", img)
cv2.waitKey()
