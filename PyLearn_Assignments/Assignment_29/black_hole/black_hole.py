import cv2
import numpy as np


for i in range(4) :

    img_1 = cv2.imread(f"black_hole/{i+1}/1.jpg").astype(dtype = np.float32)
    img_2 = cv2.imread(f"black_hole/{i+1}/2.jpg").astype(dtype = np.float32)
    img_3 = cv2.imread(f"black_hole/{i+1}/3.jpg").astype(dtype = np.float32)
    img_4 = cv2.imread(f"black_hole/{i+1}/4.jpg").astype(dtype = np.float32)
    img_5 = cv2.imread(f"black_hole/{i+1}/5.jpg").astype(dtype = np.float32)

    result = (img_1 + img_2 + img_3 + img_4 + img_5) / 5
    result = result.astype(np.uint8)

    cv2.imwrite(f"black_hole/hole_result{i+1}.jpg" , result)


image_1 = cv2.imread("black_hole\hole_result1.jpg").astype(dtype = np.float32)
image_2 = cv2.imread("black_hole\hole_result2.jpg").astype(dtype = np.float32)
image_3 = cv2.imread("black_hole\hole_result3.jpg").astype(dtype = np.float32)
image_4 = cv2.imread("black_hole\hole_result4.jpg").astype(dtype = np.float32)

top = np.concatenate((image_1,image_2) , axis=1)
botton = np.concatenate((image_3,image_4) , axis=1)

result = np.concatenate((top , botton) , axis=0)

cv2.imwrite("files/result_black_hole.jpg" , result)