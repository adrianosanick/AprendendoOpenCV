
import cv2
import numpy as np

img = cv2.imread("tampa_azul.jpg")
img_gray = cv2.imread("tampa_azul.jpg",0)

valorMedio = cv2.mean(img)
valorMedioGray = cv2.mean(img_gray)

(mean, std) = cv2.meanStdDev(img)
(means, stds) = cv2.meanStdDev(img_gray)

statsRGB = np.concatenate([(mean, std)]).flatten()
statsGray = np.concatenate([(means, stds)]).flatten()

print("Valores da media e desvio padrao RGB")
print(valorMedio)
print(statsRGB)

print("Valores da media e desvio padrao tons de cinza")
print(valorMedioGray)
print(statsGray)
