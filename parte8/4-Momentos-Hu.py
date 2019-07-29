import cv2
import numpy as np

img = cv2.imread("circle.jpg",0)

momentos = cv2.moments(img)
momentosHu = cv2.HuMoments(momentos)

print(momentosHu.flatten())

