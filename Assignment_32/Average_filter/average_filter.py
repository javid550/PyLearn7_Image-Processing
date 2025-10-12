import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Average_filter/input/1.tif" , cv2.IMREAD_GRAYSCALE)

filters = [
    np.ones((5 , 5), np.uint8) * .04 ,
    np.ones((5 , 5), np.uint8) * 1 ,
    np.ones((5 , 5), np.uint8) * 5 ,
    np.ones((3 , 3), np.uint8) * .04 ,
    np.ones((3 , 3), np.uint8) * 1 ,
    np.ones((3 , 3), np.uint8) * 5 
]

results = [cv2.filter2D(image , -1 , filter) for filter in filters]

fig , axes = plt.subplots(1 , len(results) , figsize=(15 , 5))

for ax , img , filter in zip(axes , results , filters) :
    ax.imshow(img , cmap='gray')
    ax.set_title(f"Avg-kernel {filter.shape} : {filter[0][0]}")
    plt.axis('off')

plt.suptitle("Average Filtering to Reveal Hidden Details" , fontsize=12)
plt.tight_layout()
plt.show()