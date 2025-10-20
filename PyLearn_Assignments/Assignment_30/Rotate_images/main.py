import cv2

image = cv2.imread("inputs\javid_m.jpg")

rotated = cv2.rotate(image , cv2.ROTATE_180)

cv2.imshow("Rotated image" , rotated)
cv2.imwrite("outputs/javid.jpg" , rotated)

cv2.waitKey()