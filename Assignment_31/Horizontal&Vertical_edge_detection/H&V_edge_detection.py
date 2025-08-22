import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("session_31_6\inputs\image(6).jpeg" , cv2.IMREAD_GRAYSCALE)

rows , cols = image.shape
result = np.zeros((rows , cols) , dtype=np.uint8)
results = [image]

kernel_1 = np.array([[-1 , 0 , 1],
                     [-1 , 0 , 1],
                     [-1 , 0 , 1]])

kernel_2 = np.array([[-1 , -1 , -1],
                     [ 0 , 0 , 0 ],
                     [ 1 , 1 , 1 ]])

kernels = [kernel_1 , kernel_2]

for k in kernels :
    result = np.zeros((rows , cols) , dtype=np.uint8)
    for i in range(1 , rows-1) :
        for j in range(1 , cols-1) :
            small = image[i-1:i+2 , j-1:j+2]
            edge = np.sum(k * small)
            result[i,j] = np.clip(edge , 0 , 255)
    results.append(result)

titles = ["Original_image" , "Vertical-edges_output" , "Horizontal-edges_output"]
plt.figure(figsize=(10,5))
for i, img in enumerate(results) :
    plt.subplot(1, 3, i+1)
    plt.imshow(img , cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.suptitle("horizontal & vertical edge detecting")
plt.tight_layout()
plt.show()