"""
Morphological Transformations - Erosion, Dilation, Opening, Closing
Simple Operations based on Image Shape
Performed on Binary Image using Kernel (decides the operation)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('notes.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Using dilation transformation that will remove illumiation spots?
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)

# Erosion erodes the pixels and changes the corner/boundary values when pixels in
# kernel are not all the same value
erosion = cv2.erode(mask, kernel, iterations=2)

# Opening = erosion + dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Closing = dilation + erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Difference between dilation ans erosion of an image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

# Diff between image and opening of an image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'Morph Gradient', 'Top Hat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # xticks and yticks will add/remove axes
    plt.xticks([])
    plt.yticks([])

plt.show()