import cv2
import time
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def zoom_effect(image , landmarks , zoom=2.0) :
    landmarks = np.array(landmarks, dtype=np.int32)
    x, y, w, h = cv2.boundingRect(landmarks)
    mask = np.zeros(image.shape , dtype=np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (1, 1, 1), -1)
    mask = mask // 1

    roi = image * mask
    roi = roi[y:y + h , x:x + w]
    roi_big = cv2.resize(roi, (int(w * zoom), int(h * zoom)))

    mask_crop = mask[y:y + h , x:x + w]

    mask_big = cv2.resize(mask_crop, (roi_big.shape[1], roi_big.shape[0]))

    if len(mask_big.shape) == 2 :
        mask_big = cv2.merge([mask_big]*3)

    mask_clone = (mask_big * 255).astype(np.uint8)
    center = (x + w // 2 , y + h // 2)

    output = cv2.seamlessClone(roi_big , image , mask_clone , center , cv2.NORMAL_CLONE)
    return output


fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread("inputs/Clinton.jpg")

start_time = time.perf_counter()

boxes, scores = fd.inference(image)
output = image.copy()

for pred in fa.get_landmarks(image, boxes):

    # ========== BIG LIPS ==========
    lips_indices = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
    lips_landmarks = [pred[i] for i in lips_indices]

    output = zoom_effect(output , lips_landmarks , zoom=2.0)

    # ========== BIG EYES ==========
    left_eye_indices = [89, 90, 87, 91, 93, 96, 94, 95]
    right_eye_indices = [35, 36, 33, 37, 39, 42, 40, 41]

    left_eye_landmarks = [pred[i] for i in left_eye_indices]
    right_eye_landmarks = [pred[i] for i in right_eye_indices]

    output = zoom_effect(output , left_eye_landmarks , zoom=2.0)
    output = zoom_effect(output , right_eye_landmarks , zoom=2.0)

print("Processing time:", time.perf_counter() - start_time)

cv2.imshow("Big Eyes & Lips Filter", output)
cv2.imwrite("outputs/The_result_1.jpg", output)
cv2.waitKey()