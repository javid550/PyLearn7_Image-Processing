import cv2
import numpy as np

image = cv2.imread("Median_filter\inputs\image-5.jpg" , cv2.IMREAD_GRAYSCALE)

output = cv2.medianBlur(image , 5)

result = np.hstack((image , output))

cv2.imwrite("Median_filter\outputs\median_5.jpg" , result)