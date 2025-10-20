import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def chessed_face(image) :
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray , 1.2)

    for face in faces :
        x, y, w, h = face
        face_image = image[y:y+h , x:x+w]
        face_image_small = cv2.resize(face_image , [12, 12])
        face_image_big = cv2.resize(face_image_small , [w, h] , interpolation=cv2.INTER_NEAREST)
        image[y:y+h , x:x+w] = face_image_big
    return image

def sticker(image) :
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    lion_image = cv2.imread("animal.png" , cv2.IMREAD_UNCHANGED)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray , 1.2)

    for face in faces :
        x, y, w, h = face
        sticker = cv2.resize(lion_image , [w,h])
        b , g , r , a = cv2.split(sticker)
        alpha = a / 255.0
        alpha = cv2.merge([alpha,alpha,alpha])
        roi = frame[y:y+h , x:x+w]
        sticker_bgr = cv2.merge([b,g,r])
        blended = (alpha * sticker_bgr + ( 1 - alpha) * roi).astype(np.uint8)
        frame[y:y+h , x:x+w] = blended
    return image

def glasses_lips(image) :
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    lips_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
    glasses_image = cv2.imread("glasses.png" , cv2.IMREAD_UNCHANGED)
    lips_image = cv2.imread("lips.png" , cv2.IMREAD_UNCHANGED)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray , 1.2)

    for x , y , w , h in faces :

        # -Glasses-
        gw = w 
        gh = int(h * 0.45)
        gx = x
        gy = y + int(h * 0.2)
        resized = cv2.resize(glasses_image , [gw , gh])
        b , g , r , a = cv2.split(resized)
        alpha = a / 255.0
        alpha = cv2.merge([alpha,alpha,alpha])
        roi = frame[gy:gy+gh , gx:gx+gw]
        glasses_bgr = cv2.merge([b,g,r])
        blended = (alpha * glasses_bgr + ( 1 - alpha) * roi).astype(np.uint8)
        image[gy:gy+gh , gx:gx+gw] = blended

        # -lips-
        lips = lips_detector.detectMultiScale(frame_gray[y:y+h , x:x+w] , 1.2 , 20)
        if len(lips) > 0 :
            lips = sorted( lips , key=lambda l: l[2]*l[3] , reverse=True )[0]
            lx , ly , lw , lh = lips
            lx += x
            ly += y
            resized_lips = cv2.resize(lips_image , (lw , lh))
            b , g , r , a = cv2.split(resized_lips)
            alpha = a / 255.0
            alpha = cv2.merge([alpha,alpha,alpha])
            roi = image[ly:ly+lh , lx:lx+lw]
            lips_bgr = cv2.merge([b,g,r])
            blend = (alpha * lips_bgr + ( 1 - alpha) * roi).astype(np.uint8)
            image[ly:ly+lh , lx:lx+lw] = blend
    return image


def mirror(image) :
    _ , w = image.shape[:2]
    half = w // 2
    left_half = image[:, half:]
    flipped = cv2.flip(left_half , 1)
    image[:, :half] = flipped
    return image


state = 0

while True:

    _ , frame = cap.read()

    if state == 1 :
        frame = sticker(frame)
    elif state == 2 :
        frame = glasses_lips(frame)
    elif state == 3 :
        frame = chessed_face(frame)
    elif state == 4 :
        frame = mirror(frame)

    cv2.imshow("Image filtering", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 :
        break
    elif key == ord('1') :
        state = 1
    elif key == ord('2') :
        state = 2
    elif key == ord('3') :
        state = 3
    elif key == ord('4') :
        state = 4

cap.release()
cv2.destroyAllWindows()