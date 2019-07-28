import cv2 as cv

img1 = cv.imread('C:\\Users\\megan\\Desktop\\Curso Udemy - Visao computacional com Python e OpenCV\\Parte 3\\Imagens\\Superman.png')
img2 = cv.imread('C:\\Users\\megan\\Desktop\\Curso Udemy - Visao computacional com Python e OpenCV\Parte 3\\Imagens\\batman.png')

imgSub = cv.suctract(img1, img2)

cv.imshow("Imagem Subtraida", imgSub)
cv.waitKey(0)
cv.destroyAllWindows()
