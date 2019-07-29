import cv2
import numpy as np

im = cv2.imread("triangle.jpg", 0)

tipo = cv2.THRESH_BINARY_INV
_, imgBin = cv2.threshold(im, 0, 255, tipo)

modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
_,contorno, hierarquia = cv2.findContours(imgBin, modo, metodo)



if len(contorno) > 0:
    obj = contorno[0]
    area = cv2.contourArea(obj)
    print area

    perimetro = cv2.arcLength(obj, True)
    print perimetro

else:
    print("sem contorno encontrado")

    
    

