import cv2
import numpy as np

img = cv2.imread('hospital2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.01)

dst = cv2.dilate(dst, None)

img[dst > 0.01*dst.max()] = [0,0,255]

cv2.imshow('Harris', img)
cv2.waitKey()
