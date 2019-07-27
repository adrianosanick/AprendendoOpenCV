import cv2 as cv
import numpy as np

imgOriginal = cv.imread("C:\Users\megan\Desktop\Curso Udemy - Visao computacional com Python e OpenCV\Parte 3\Imagens\einstein.jpg", 0)
totalLinhas, totalColunas = imgOriginal.shape

mat = cv.getRotationMatrix2D((totalColunas/2, totalLinhas/2), 45,1)

imgRotacionada = cv.warpAffine(imgOriginal, mat, (totalColunas, totalLinhas))

cv.imshow("Imagem rotacionada 45", imgRotacionada)
cv.waitKey(0)
cv.destroyAllWindows()
