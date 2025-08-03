import cv2 

image = cv2.imread("me.jpg" , 0)

inverted = 255 - image
blured = cv2.GaussianBlur(inverted , (21,21) , 0)
inverted_blured = 255 - blured

sketch = image / inverted_blured
sketch = sketch * 255

cv2.imwrite("files/result_sketch.jpg" , sketch)