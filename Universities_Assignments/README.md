# Computer-Vision_Assignment

## Image-Processing _ University

### What's there : 

- There are two folders in this assignment with names of :
  - *Affinity* , *filtering* :
    - filtering : The flies of this folder apply two filters , **Big-Face_filter** and **waved_filter**
    - Affinity : Apply four affinity conversions on image
      - resize_image : Resize image in different ways
      - rotate_image : Apply 45 degree rotation
      - transfer_image : Transfer image with specified pixel scale from one side to another or both sides
      - tilt_image : To tilt an image horizontally or vertically 
  - All these practices were implemented using the *OpenCV* library

## Outputs :

### **Filtering**

#### Face_Stretch :

Input:
 ![Input](filtering\face_stretch\input/man.jpg)

Output:
 ![Output](Universities-Assignments/filtering/face_stretch/output/stretched-man.jpg)

#### Wave_distortion :

Input:
 ![Input](Universities-Assignments/filtering/wave_distortion/input/Lena.jpg)

Output:
 ![Output](Universities-Assignments\filtering\wave_distortion\output/waved_Lena.jpg)



### **Affinity**

#### Resize : 

Input:
 ![Input](Universities-Assignments/Affinity/resize_image/input/home.jpg)

Outputs:
 ![Output](Universities-Assignments/Affinity/resize_image/outputs/resized-image1.jpg)
 ![Output](Universities-Assignments/Affinity/resize_image/outputs/resized-image2.jpg)
 ![Output](Universities-Assignments/Affinity/resize_image/outputs/resized-image3.jpg)
 ![Output](Universities-Assignments/Affinity/resize_image/outputs/resized-image4.jpg)
 
#### Rotate : 

Input:
 ![Input](Universities-Assignments/Affinity/rotate_image/input/home.jpg) 

Output:
 ![Output](Universities-Assignments/Affinity/rotate_image/output/rotated_45.jpg)
 
#### Tilt :

Input:
 ![Input](Universities-Assignments/Affinity/tilt_image/input/home.jpg) 

Outputs :
 ![Output](Universities-Assignments/Affinity/tilt_image/outputs/horizontal_tilted.jpg)
 ![Output](Universities-Assignments/Affinity/tilt_image/outputs/vertical_tilted.jpg)
 
### Transfer :

Input:
 ![Input](Universities-Assignments/Affinity/transfer_image/input/home.jpg) 
 
Outputs :
 ![Output](Universities-Assignments/Affinity/transfer_image/outputs/transfered-image1)
 ![Output](Universities-Assignments/Affinity/transfer_image/outputs/transfered-image2)
 ![Output](Universities-Assignments/Affinity/transfer_image/outputs/transfered-image3)
 

### Installation guide for python files
To execute this program you need to install a library

**OpenCV**  , **numpy** 

You can install them by using the *pip* command :

For instance :
**pip install OpenCV**

Note : for importing OpenCV library you need this command :
```
import cv2
```

## How To Run

To run python files , open your *cmd* or *Terminal* and enter this command :
```
python "file_name".py
```
