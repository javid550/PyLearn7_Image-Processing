import cv2 
import numpy as np

video = cv2.VideoCapture("files\cars.mp4")

frame_id = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

frames = []
for fid in frame_id :
    video.set(cv2.CAP_PROP_POS_FRAMES , fid)
    ret , frame = video.read()
    frames.append(frame)

org_frame = np.average(frames , axis=0).astype(dtype = np.uint8)

cv2.imwrite("files/result_cars.jpg" , org_frame)