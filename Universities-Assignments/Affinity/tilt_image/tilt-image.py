import cv2 
import numpy as np

image = cv2.imread("Univercities-Assignments\Affinity\outputs\home.jpg")

h , w = image.shape[:2]

result = np.zeros((int(h*1), int(w*1.27), 3), dtype=np.uint8)

kernel = np.array([[1 , 0.3 , 0],
                   [0 , 1 , 0],
                   [0 , 0 , 1]])

for y in range(h) :
    for x in range(w) :
        x_new = int(kernel[0,0]*x + kernel[0,1]*y + kernel[0,2])
        y_new = int(kernel[1,0]*x + kernel[1,1]*y + kernel[1,2])

        if 0 <= x_new < result.shape[1] and 0 <= y_new < result.shape[0] :
            result[y_new , x_new] = image[y , x]

cv2.imwrite("Univercities-Assignments/Affinity\outputs/tilted-image2.jpg" , result)