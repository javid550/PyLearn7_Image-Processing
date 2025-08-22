# Assignment 31

## Image-Processing _ 6

### What's there : 

- There are five folder in this assignment with names of :
  - *Horizontal&Vertical_edge_detection* , *Noise_reduction* , *Edge_detection* , *Histogram* , *Blurred*
    - Horizontal&Vertical_edge_detection : Detecting , horizontal and vertical edges from image
    - Noise_reduction : Get an image as input and reducing noises with three different kernels
    - Histogram : calculate and draw histogram for (0-255) , dark to light color of an image
    - Blurred : This file get an image as input and blurred the background
    - Edge_detection : It can detect the edges from an image 
  - All these practices were implemented using the *OpenCV* library

## Outputs :

### Herizontal&Vertical_edge_detection :

Input : ![Input](Horizontal&Vertical_edge_detection/input.jpeg) 

 Output : ![Output](Horizontal&Vertical_edge_detection/output.png)

### Blurred : 

Input : ![Input](Blurred/input.jpeg) 

 Output : ![Output](Blurred/output.png)
 
### Histogram :

 Output_plt.plot() : ![Output](Histogram/Figure_1.png)
 
 Output_plt.hist() : ![Output](Histogram/Figure_2.png)
 
 Output_plt.bar() : ![Output](Histogram/Figure_3.png)

### Edge_detection :

Input : ![Input](Edge_detection/input_1.jpeg) 

 Output : ![Output](Edge_detection/output_1.png)

Input : ![Input](Edge_detection/input_2.jpeg) 

 Output : ![Output](Edge_detection/output_2.png)

### Noise_reduction :

Input : ![Input](Noise_reduction/input_1.jpeg) 

 Output : ![Output](Noise_reduction/output_1.png)

Input : ![Input](Noise_reduction/input_2.jpeg) 

 Output : ![Output](Noise_reduction/output_2.png)
 
Input : ![Input](Noise_reduction/input_3.jpeg) 

 Output : ![Output](Noise_reduction/output_3.png)


### Installation guide for python files
To execute this program you need to install a library

**OpenCV**  , **numpy** , **matplotlib**

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
