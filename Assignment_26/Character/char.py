import cv2

image = cv2.imread("session 26_1\white.png")
image = cv2.resize(image , (500 , 500))

cv2.line(image , (300,200) , (300,300) , (0,0,0) , 10)
cv2.ellipse(image , (270,300) , (30,30) , 0 , 0 , 180 , (0,0,0), 10)

cv2.imshow("Character J" , image)
cv2.imwrite("J.jpg" , image)

cv2.waitKey()