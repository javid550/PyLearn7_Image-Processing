import cv2 
import numpy as np
import math

image = cv2.imread("Univercities-Assignments\Affinity\input\home.jpg")
h , w = image.shape[:2]

theta = math.radians(45)
sin_t = math.sin(theta)
cos_t = math.cos(theta)

cx , cy = w//2 , h//2  # center of image
new_w , new_h = int(w*1.27), int(h*1.6)
ox , oy = new_w//2 , new_h//2
result = np.zeros((new_h , new_w , 3) , np.uint8)

for y in range(new_h) :
    for x in range(new_w) :
        x_shift = (x - ox)
        y_shift = (y - oy)
        src_x = cos_t * x_shift + sin_t * y_shift + cx
        src_y = -sin_t * x_shift + cos_t * y_shift + cy
        x_new = int(cx + x_shift * cos_t - y_shift * sin_t)
        y_new = int(cy + x_shift * sin_t + y_shift * cos_t)

        if 0 <= src_x < w and 0 <= src_y < h :
            result[y , x] = image[int(src_y) , int(src_x)]

cv2.imwrite("Univercities-Assignments\Affinity\outputs/rotated-image.jpg" , result)