import cv2
import imageio
import numpy as np

frames = []

while True:
    frame = np.random.random((250,350)) * 255
    frame = np.array(frame, dtype = np.uint8)

    frames.append(frame)

    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break

imageio.mimsave("noise.gif" , frames , duration=0.2)