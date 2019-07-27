import cv2 as cv
import numpy as np

imgOriginal = cv.imread("C:\Users\megan\Desktop\Curso Udemy - Visao computacional com Python e OpenCV\Parte 3\Imagens\einstein.jpg")

imgModificada = cv.resize(imgOriginal, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)

cv.imshow("Imagem Original", imgOriginal)
cv.imshow("Imagem Modificada", imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()
