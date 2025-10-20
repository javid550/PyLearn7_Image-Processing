<<<<<<< HEAD
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

=======
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

>>>>>>> 282ab337581f22333ad21419c7e4fb86854640d2
cv2.imwrite("Univercities-Assignments/filtering\outputs/waved-lenna.jpg" , result)