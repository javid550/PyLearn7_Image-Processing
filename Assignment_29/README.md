# Assignment 29

## Image-Processing _ 4

### What's there :

- There are six folder in this assignment with names of :
  - *black_hole* , *cars_background* , *change_decoration* , *face_morphing* , *photo_to_sketch* , *sabtract_images*
    - change_decoration : This file apply changes on floor of input image by masking images
    - cars_background : To get a **.mp4** file as input and give background of that video file
    - photo_to_sketch : You can give your photo as input and this file change it to sketch
    - sabtract_images : With subtraction ability you can make new images
    - face_morphing : Morph images and concatenate them
    - black_hole : Resolve noises of images
      - read images from a folder , remove the noise of images and generate a cleaner image
      - here some guidance :
        -  **hole_result1.jpg** is output of the folder with name of **1**
        -  **hole_result2.jpg** is output of the folder with name of **2**
        -  **hole_result3.jpg** is output of the folder with name of **3**
        -  **hole_result4.jpg** is output of the folder with name of **4**
      - After generate cleaner version of each part , concatenate them and make a *black hole* image without noise
  - All these practices were implemented using the *OpenCV* library

## Outputs :

### Black_hole :

Output : ![Screenshot](black_hole/result_black_hole.jpg)

### Cars_background :

Output : ![Output](cars_background/cars_output.jpg)

### Photo_to_sketch :

Input : ![Screenshot](photo_to_sketch/input.jpg) 

 Output : ![Screenshot](photo_to_sketch/output.png)

### Face_motphing :

Input_1 : ![Screenshot](face_morphing/input_1.jpg)
Input_2 : ![Screenshot](face_morphing/input_2.jpg)

 Output : ![Screenshot](face_morphing/output.jpg)

 ### Subtract_images :

Input_1 : ![Screenshot](sabtract_images/input_1.jpeg)
Input_2 : ![Screenshot](sabtract_images/input_2.jpeg)

 Output : ![Screenshot](sabtract_images/sub_output.jpg)

### Change_decoration :

Input_1 : ![Screenshot](change_decoration/decoration_input.jpeg)
Input_2 : ![Screenshot](change_decoration/floor_input.jpeg)
Input_3 : ![Screenshot](change_decoration/mask_input.jpeg)

 Output : ![Screenshot](change_decoration/output.jpg)

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
python ( cat_face.py / football.py / filter.py )
```
