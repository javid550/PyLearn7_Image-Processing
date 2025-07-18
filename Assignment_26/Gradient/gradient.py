import cv2

image = cv2.imread("session 26_1\white.png")
image = cv2.resize(image , (500 , 500))

for x in range(500) :
    shade = int((x / 499) * 255)
    cv2.line(image , (0,x) , (499,x) , (shade,shade,shade) , 1)

cv2.imshow("Gradient" , image)
cv2.imwrite("gradient.jpg" , image)

cv2.waitKey()