"""
Image gradient is directional change in intensity or colour of
an image.
Laplacian
SobelX - Joint Gaussian and Differentiation operations
SobelY
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# Convert then to unsigned int
lap = np.uint8(np.abs(lap))

# dx = 1, dy = 0, meaning first order derivative on the X axis
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX, sobelY)
titles = ['image', 'Laplacian', 'Sobel X', 'Sobel Y', 'SobelOR']
images = [img, lap, sobelX, sobelY, sobel]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # xticks and yticks will add/remove axes
    plt.xticks([])
    plt.yticks([])

plt.show()