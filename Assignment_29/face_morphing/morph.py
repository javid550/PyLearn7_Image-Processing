import cv2
import numpy as np

young_image = cv2.imread("young.jpg")
old_image = cv2.imread("old.jpg")

young_image = cv2.resize(young_image , (540,540))
old_image = cv2.resize(old_image , (540,540))

young_image = young_image.astype(np.float32)
old_image = old_image.astype(np.float32)

image_1 = (old_image*1/4 + young_image*3/4)
image_2 = (old_image*2/4 + young_image*2/4)
image_3 = (old_image*3/4 + young_image*1/4)

image_1 = image_1.astype(np.uint8)
image_2 = image_2.astype(np.uint8)
image_3 = image_3.astype(np.uint8)

result = np.concatenate((young_image , image_1 , image_2 , image_3 , old_image) , axis=1)

cv2.imwrite("files/result_morph.jpg" , result)