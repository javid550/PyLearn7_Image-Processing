import cv2 
import numpy as np

def blur(img , kernel_size=5) :
    pad = kernel_size // 2
    image_padded = np.pad(img , ((pad,pad) , (pad,pad) , (0,0)) , mode='reflect')
    blurred = np.zeros_like(img)

    for i in range(img.shape[0]) :
        for j in range(img.shape[1]) :
            region = image_padded[i:i+kernel_size , j:j+kernel_size]
            blurred[i , j] = np.mean(region , axis=(0 , 1))

    return blurred.astype(np.uint8)

img = cv2.imread("session_31_6/inputs/flower.jpeg")
hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

lower_color = np.array([0 , 0 , 190])
upper_color = np.array([255 , 250 , 255])
mask = cv2.inRange(hsv , lower_color , upper_color)
mask_3ch = cv2.merge([mask,mask,mask])

blurred = blur(img , kernel_size=20)

focused = np.where(mask_3ch == 255 , img , blurred)

cv2.imshow("Focused Flower" , focused)
cv2.imwrite("session_31_6\output/out.png" , focused)
cv2.waitKey()