import cv2
import random

image = cv2.imread("landscape\snowy.jpg")

height , width = image.shape[:2]

num_frames = 100
num_snowflakes = 200

snowflakes = [{'x' : random.randint(0,width) , 'y' : random.randint(-height,0)} for _ in range(num_snowflakes)]

frames = []

while True :
    for frame in range(num_frames) :
        frame = image.copy()

        for flake in snowflakes :
            flake['y'] += random.randint(2,5)

            if flake['y'] > height :
                flake['y'] = random.randint(-50 , 0)
                flake['x'] = random.randint(0,width)

            cv2.circle(frame, (flake['x'],flake['y']), 3 , (255,255,255), -5)

        rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        frames.append(rgb_frame)

    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break
