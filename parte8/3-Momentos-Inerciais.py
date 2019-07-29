import cv2

img = cv2.imread("circle.jpg", 0)

momentos = cv2.moments(img)

print(len(momentos))

print(momentos)

area = momentos['m00']
print("Area")
print(area)

X = momentos['m10']/area
Y = momentos['m01']/area

print("Medias")
print(X)
print(Y)

cx = int(momentos['m10']/momentos['m00'])
cy = int(momentos['m01']/momentos['m00'])

print("centroide")
print(cx)
print(cy)
