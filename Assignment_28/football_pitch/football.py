import cv2
import numpy as np

width , height = 800 , 500 

pitch = np.zeros((height , width , 3) , dtype = np.uint8)
pitch[:] = (0,128,0)

white = (255,255,255)


cv2.rectangle(pitch, (50 , 30) , (750,470) , white , 2)
cv2.line(pitch, (400,30) , (400,470) , white , 2)
cv2.circle(pitch, (400,250) , 60 , white , 2)
cv2.circle(pitch, (400,250) , 4 , white , 3)

cv2.rectangle(pitch, (50 , 150) , (150,350) , white , 2)
cv2.rectangle(pitch, (650 , 150) , (750,350) , white , 2)

cv2.rectangle(pitch, (50 , 200) , (90,300) , white , 2)
cv2.rectangle(pitch, (710 , 200) , (750,300) , white , 2)

cv2.circle(pitch, (120,250) , 2 , white , -1)
cv2.circle(pitch, (680,250) , 2 , white , -1)

cv2.imshow("Football Pitch" , pitch)
cv2.waitKey()