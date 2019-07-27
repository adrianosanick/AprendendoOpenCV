import cv2 
import numpy as np

imgOriginal = cv2.imread("imagens/einstein.jpg",0)

totalLinhas, totalColunas = imgOriginal.shape[:2]

matriz = np.float32([[1,0,100],[0,1,100]])
imgDeslocada = cv2.warpAffine(imgOriginal, matriz, (totalColunas, totalLinhas))

cv2.imshow("Imagem Deslocada", imgDeslocada)
cv2.waitKey(0)
cv2.destroyAllWindows()
