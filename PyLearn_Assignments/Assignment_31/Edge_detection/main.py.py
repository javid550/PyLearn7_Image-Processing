import cv2
import numpy as np

def edge_detection(image) :

    image = cv2.imread(image , cv2.IMREAD_GRAYSCALE)

    rows , cols = image.shape
    result = np.zeros((rows , cols) , dtype=np.uint8)

    kernel = np.array([[-1 , -1 , -1],
                       [-1 , 8 , -1],
                       [-1 , -1 , -1]])

    for i in range(1 , rows-1) :
        for j in range(1 , cols-1) :
            small = image[i-1:i+2 , j-1:j+2]
            edge = np.sum(kernel * small)
            result[i,j] = np.clip(edge , 0 , 255)

    cv2.imshow("Edge_detection" , result)
    cv2.waitKey()

image_1 = edge_detection("input_1.jpeg")
image_2 = edge_detection("input_2.jpeg")