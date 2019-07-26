import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\\megan\\Desktop\\Curso Udemy - Visao computacional com Python e OpenCV\\Parte 3\\Imagens\\Cinza.jpg")

plt.hist(img.ravel(), 256, [0,256])
plt.show()

