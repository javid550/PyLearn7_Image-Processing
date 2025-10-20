import cv2 
import numpy as np
import math

image = cv2.imread("Univercities-Assignments/filtering\inputs\Lena.jpg")

h , w = image.shape[:2]

result = np.zeros_like(image)

for y in range(h) :
    for x in range(w) :

        x_new = int(x + 10 * math.sin(3 * math.pi * y / 30))
        y_new = y

        if 0 <= x_new < w and 0 <= y_new < h :
            result[y_new , x_new] = image[y , x]

cv2.imwrite("Univercities-Assignments/filtering\outputs/waved-lenna.jpg" , result)