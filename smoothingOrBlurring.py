"""
Many blurring filters available - Homogeneous, Gaussian, Median, Bilateral
Homogeneous Filter - All pixels contribute equal weight
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))

# Gaussian Filter - different-weight-kernel in both x and y directions,
# better hgih frequency noise reduction
gauss = cv2.GaussianBlur(img, (5, 5), 0)

# Median Filter best to deal with salt and pepper noise
median = cv2.medianBlur(img, 5)

# Bilateral Filter - preserves the edges while removing noise
bil = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Conv', 'Blur', 'Gaussian', 'Median', 'Bilateral']
images = [img, dst, blur, gauss, median, bil]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # xticks and yticks will add/remove axes
    plt.xticks([])
    plt.yticks([])

plt.show()