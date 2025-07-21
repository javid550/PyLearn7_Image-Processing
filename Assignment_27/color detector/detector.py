import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened() :
    print("Cannot access webcam.")
    exit()

while True:

    _ , frame = cap.read()

    if not _ :
        print("Falied to grap frames !!!")
        continue

    frame = cv2.resize(frame , (640 , 480))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    height , width = gray.shape[:2]

    box_size = 60 

    center_x , center_y = width // 2 , height // 2 
    half_box = box_size // 2

    x1 = center_x - half_box
    y1 = center_y - half_box
    x2 = center_x + half_box
    y2 = center_y + half_box

    x1 = max(x1 , 0)
    y1 = max(y1 , 0)
    x2 = min(x2 , width)
    y2 = min(y2 , height)


    roi = gray[y1:y2 , x1:x2]

    if roi.size > 0 :
        avg_intensity = int(np.mean(roi))
    else :
        avg_intensity = 0 
        print("ROI is empty")

    if avg_intensity < 50 :
        color_name = "Black"
    elif avg_intensity > 150 :
        color_name = "White"
    else :
        color_name = "Gray"

    # dimmed = (gray * 0.4).astype(np.uint8)
    # dimmed[y1:y2 , x1:x2] = gray[y1:y2 , x1:x2]

    blurred = cv2.GaussianBlur(gray, (71,71) , 0)
    blurred[y1:y2 , x1:x2] = gray[y1:y2 , x1:x2]

    cv2.rectangle(blurred , (x1 , y1) , (x2 , y2) , (0,0,0) , 2)
    cv2.putText(blurred , color_name , (20 , 50) , cv2.FONT_HERSHEY_SIMPLEX , 1.5 , (0,0,0) , 3 , cv2.LINE_AA)

    cv2.imshow("Color Detestor", blurred) 
    
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()