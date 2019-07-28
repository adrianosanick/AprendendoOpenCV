import cv2 as cv

img1 = cv.imread("parte3/imagens/batman.png",0)
img2 = cv.imread("parte3/imagens/superman.png",0)

imgTotal = cv.addWeighted(img1, 0.8, img2, 1.0, 0)

cv.imshow("Imagem Mesclada", imgTotal)
cv.waitKey(0)
cv.destroyAllWindows()