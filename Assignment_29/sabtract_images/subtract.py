import cv2

image_1 = cv2.imread("files\image(1).jpeg")
image_2 = cv2.imread("files\image.jpeg")

result = cv2.subtract(image_1 , image_2)
result = 255 - result

cv2.imwrite("files/sub_result.jpg" , result)