import cv2

image = cv2.imread("Batman\Bat.jpg")
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

_ , image = cv2.threshold(image , 100 , 255 , cv2.THRESH_BINARY_INV)

cv2.putText(image , "BatMan" , (360,450) , cv2.FONT_HERSHEY_SIMPLEX , 1.5 , 255 , 3)

cv2.imshow("Batman🦇" , image)
cv2.waitKey()

cv2.imwrite("batman.jpg" , image)