import cv2
import numpy as np
import matplotlib.pyplot as plt

image_low_contrast = cv2.imread("Histogram_Equalization\inputs\low-contrast_3.jpg" , cv2.IMREAD_GRAYSCALE)
hist_low = cv2.calcHist([image_low_contrast] , [0] , None , [256] , [0 , 256])

image_high_contrast = cv2.equalizeHist(image_low_contrast)
hist_high = cv2.calcHist([image_high_contrast] , [0] , None , [256] , [0 , 256])

clahe = cv2.createCLAHE(clipLimit=2.0 , tileGridSize=(8 , 8))
image_clahe_contrast = clahe.apply(image_low_contrast)

result = np.hstack((image_low_contrast , image_high_contrast , image_clahe_contrast))
cv2.imwrite("Histogram_Equalization\outputs\high_contrast_3.jpg" , result)

# plt.plot(hist_high)
# plt.show()