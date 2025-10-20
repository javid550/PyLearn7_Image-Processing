import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image_path) :
    img = cv2.imread(image_path , cv2.IMREAD_GRAYSCALE)
    if img is None :
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    pixels = img.ravel()

    hist = np.zeros(256 , dtype=int)

    for value in pixels :
        hist[value] += 1

    return hist , img

hist , img = calculate_histogram("session_31_6\inputs\galaxy2.jpg")

plt.figure(figsize=(15,15))

# 1. Using plt.plot()
plt.subplot(1 , 3 , 1)
plt.plot(hist , color='red')
plt.title("Histogram - plt.plot()")
plt.xlabel("Pixeel Value")
plt.ylabel("Frequency")

# 2. Using plt.hist()
plt.subplot(1 , 3 , 2)
plt.hist(img.ravel() , bins=256 , range=(0,256) , color='green')
plt.title("Histogram - plt.hist()")
plt.xlabel("Pixeel Value")
plt.ylabel("Frequency")

# 3. Using plt.bar()
plt.subplot(1 , 3 , 3)
plt.bar(np.arange(256) , hist , color='blue' , width=1)
plt.title("Histogram - plt.bar()")
plt.xlabel("Pixeel Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()