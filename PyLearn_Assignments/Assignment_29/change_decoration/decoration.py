import cv2
import numpy as np

image_home = cv2.imread("image(5).jpeg")
image_floor = cv2.imread("image(6).jpeg")
image_mask = cv2.imread("image(7).jpeg")

_mask = image_mask / 255.0
new_floor = image_floor * _mask

home = cv2.resize(image_home , (image_floor.shape[1] , image_floor.shape[0]))
home = home.astype(np.float32)
mask = image_mask.astype(np.float32)

new_decor =+ mask / 255 * image_floor

mask = 255 - mask 

new_decor =+ mask / 255 * home

result = new_decor + new_floor
result = result.astype(np.uint8)

cv2.imwrite("files/new_decor.jpg" , result)