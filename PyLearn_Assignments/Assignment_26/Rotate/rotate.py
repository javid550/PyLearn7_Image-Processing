import cv2

image = cv2.imread("session 26_1\Rotate\sad_mans.jpg")

rotated = cv2.rotate(image , cv2.ROTATE_180)

cv2.imshow("Rotated image" , rotated)
cv2.imwrite("happy_man.jpg" , rotated)

cv2.waitKey()