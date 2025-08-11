import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def get_landmarks(frame, face_organ):
    land_mark = []
    boxes, scores = fd.inference(frame)

    for pred in fa.get_landmarks(frame, boxes):
        if face_organ == "lips":
            idx = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
        elif face_organ == "left_eye":
            idx = [35, 41, 40, 42, 39, 37, 33, 36]
        elif face_organ == "right_eye":
            idx = [89, 90, 87, 91, 93, 96, 94, 95]
        else:
            idx = []
        for i in idx:
            land_mark.append(pred[i])
    return land_mark


def make_filter_from_face(land_mark, main_img, target_size=None):
    land_mark = np.array(land_mark, dtype=int)
    x, y, w, h = cv2.boundingRect(land_mark)

    mask = np.ones_like(main_img, np.uint8) * 255
    cv2.drawContours(mask, [land_mark], -1, (0, 0, 0), -1)
    mask = np.where(mask == (0, 0, 0), main_img, mask)
    crop = mask[y:y + h, x:x + w]

    if target_size:
        crop = cv2.resize(crop, target_size)
         
    return crop


def put_filter_on_face(foreground, background, position):
    x, y = position
    h, w = foreground.shape[:2]

    if y + h > background.shape[0]:
        h = background.shape[0] - y
        foreground = foreground[:h, :]
    if x + w > background.shape[1]:
        w = background.shape[1] - x
        foreground = foreground[:, :w]

    gray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) / 255.0

    roi = background[y:y + h, x:x + w].astype(float)
    fg = foreground.astype(float)
    blended = (fg * mask_rgb + roi * (1 - mask_rgb)).astype(np.uint8)

    background[y:y + h, x:x + w] = blended
    return background


fd = UltraLightFaceDetecion("session_30_5/OpenVtuber/weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("session_30_5/OpenVtuber/weights/coor_2d106.tflite")

img = cv2.imread("session_30_5/session/Clinton.jpg")
fruit = cv2.imread("session_30_5/session/apple.jpg")

scale_x = fruit.shape[1] / img.shape[1]
scale_y = fruit.shape[0] / img.shape[0]

for organ in ["lips", "right_eye", "left_eye"]:
    landmarks = get_landmarks(img, organ)
    landmarks_scaled = [(int(x * scale_x), int(y * scale_y)) for x, y in landmarks]

    x, y, w, h = cv2.boundingRect(np.array(landmarks_scaled))
    
    scale_factor = 2.0
    # new_w = int(w * scale_factor)
    new_h = int(h * scale_factor)

    # x -= (new_w - w) // 2
    y -= (new_h - h) // 2

    filter_img = make_filter_from_face(landmarks, img, target_size=(w, new_h))
    fruit = put_filter_on_face(filter_img, fruit, (x, y))

# cv2.imshow("result", fruit)
cv2.imwrite("session_30_5\session\outputs/output.jpg", fruit)
# cv2.waitKey()