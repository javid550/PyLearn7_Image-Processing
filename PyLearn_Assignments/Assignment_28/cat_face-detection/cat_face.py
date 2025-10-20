import cv2

image = cv2.imread("cats.jpg")
image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
faces = face_detector.detectMultiScale(image_gray , 1.2)

for i,face in enumerate(faces) :
    x, y, w, h = face
    cv2.rectangle(image , [x , y] , [x+w , y+h] , (0,200,0) , 8)

cv2.putText(image , f"Number of cats : {len(faces)}" , (50 , 60) , cv2.FONT_HERSHEY_PLAIN , 2 , (0,0,0) , 2)

cv2.imshow("result" , image)
cv2.waitKey()