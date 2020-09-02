"""
Adaptive thresholding that uses a region of pixels to find
a threshold for that specific small region - gives better results given varying
illumination
"""

import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)

# Global threshold will darken a lot of the regions due to illumination
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive methods : cv2.ADAPTIVE_THRESH_MEAN_C = Mean of neighbourhood area
# Adaptive methods : cv2.ADAPTIVE_THRESH_GAUSSIAN_C = Weighted sum of neighbourhood area
#                    where the weights are the Gaussian window
# Last variable is a constant that is subtracted from the mean - varying changes noise in output

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5);
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5);

cv2.imshow("Image", img)
cv2.imshow("Original Image", th1)
cv2.imshow("Adaptive Mean Thresholding", th2)
cv2.imshow("Adaptive Gaussian Thresholding", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()