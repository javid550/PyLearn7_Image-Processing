import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_noise(image) :

    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)   
    
    kernel_sizes = [3 , 5 , 15]
    results = [image]

    for i , k in enumerate(kernel_sizes) :

        padding = (k - 1) // 2

        kernel = np.ones((k , k) , dtype=np.uint8) / (k ** 2)

        rows , cols = image.shape 
        result = np.zeros((rows , cols) , dtype=np.uint8)

        for row in range(padding , rows-padding) :
            for col in range(padding , cols-padding) :
                small = image[
                                row-padding : row+padding+1 ,
                                col-padding : col+padding+1
                            ]
                pixel_value = np.sum(small * kernel)
                result[row , col] = pixel_value

        results.append(result)

    titles = ["Original_image" , "Output_Kenel-3x3" , "Output_Kenel-5x5" , "Output_Kenel-15x15"]
    plt.figure(figsize=(10,5))
    for i, img in enumerate(results) :
        plt.subplot(2, 2, i+1)
        plt.imshow(img , cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.suptitle("Noise - reduction")
    plt.tight_layout()
    plt.show()

image_1 = remove_noise("session_31_6\inputs\image(7).jpeg")
image_2 = remove_noise("session_31_6\inputs\image(9).jpeg")
image_3 = remove_noise("session_31_6\inputs\image(10).jpeg")