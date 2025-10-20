import cv2 
import numpy as np
import math

image = cv2.imread("Univercities-Assignments/filtering\inputs\man.jpg" , cv2.IMREAD_GRAYSCALE)

h , w = image.shape

result = np.zeros_like(image)

cx , cy = w//2 , h//2

for y in range(h):
    for x in range(w):
        dx = (x - cx) / (w/2)
        dy = (y - cy) / (h/2)
        r = math.sqrt(dx*dx + dy*dy)
        
        # اگر نزدیک مرکز بود، scale بزرگتر
        if r < 0.8:
            scale = 1 + 0.8 * (1 - r/0.8)
        else:
            scale = 1
        
        src_x = int(cx + dx * (w/2) / scale)
        src_y = int(cy + dy * (h/2) / scale)

        if 0 <= src_x < w and 0 <= src_y < h:
            result[y, x] = image[src_y, src_x]

cv2.imwrite("Univercities-Assignments/filtering\outputs/stretched-man1.jpg" , result)