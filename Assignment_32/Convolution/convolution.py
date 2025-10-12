import cv2
import numpy as np

input = cv2.imread("Convolution\inputs\input_2.jpeg")

# 1. Edge detection filter
# kernel = np.array([[-1 , -1 , -1],
#                    [-1 , 8 , -1],
#                    [-1 , -1 , -1]])

# 2. Sharpening filter
# kernel = np.array([[0 , -1 , 0],
#                    [-1 , 5 , -1],
#                    [0 , -1 , 0]])

# 3. Emboss filter
# kernel = np.array([[-2 , -1 , 0],
#                    [-1 , 1 , 1],
#                    [0 , 1 , 2]])

# 4. Identity filter
# kernel = np.array([[0 , 0 , 0],
#                    [0 , 1 , 0],
#                    [0 , 0 , 0]])

# 5. My filter
kernel = np.array([[-3 , 0 , 3],
                   [-3 , 0 , 3],
                   [-3 , 0 , 3]])

output = cv2.filter2D(input , -1 , kernel)

result = np.hstack((input , output))

cv2.imwrite("Convolution\outputs\my-filter.jpg" , result)