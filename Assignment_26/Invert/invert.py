import cv2

image_1 = cv2.imread("session 26_1\Invert_man.jpg")
image_2 = cv2.imread("session 26_1\Invert_woman.jpg")

inverted_1 = cv2.bitwise_not(image_1)
inverted_2 = cv2.bitwise_not(image_2)

cv2.imshow("Inverted_1.jpg" , inverted_1)
cv2.imwrite("inverted_1.jpg" , inverted_1)

cv2.imshow("Inverted_2.jpg" , inverted_2)
cv2.imwrite("inverted_2.jpg" , inverted_2)

cv2.waitKey()