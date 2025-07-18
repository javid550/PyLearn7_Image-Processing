import cv2

image = cv2.imread("session 26_1\Death\mr_mouse.jpg")

height , width = image.shape[:2]

thickness = int(min(width,height) * 0.05)

start_point = (250,0) 
end_point = (0,250)

cv2.line(image , start_point, end_point, (0,0,0) , thickness)

cv2.imshow("Dead mouse" , image)
cv2.imwrite("Death.jpg" , image)

cv2.waitKey()