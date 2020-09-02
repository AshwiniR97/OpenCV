"""
To work with images of different resolutions.
We create images of diff resolutions and search for our obj
Reducing resolution as we go up the pyramid
Gaussian Pyramind - Repeated filtering and subsampling
Laplacian Pyramid - no exclusive func - use Gaussian pyramid for this
^ Difference between gaussian pyr and expanded ver of upper level in gauss
They help blend and recreate/reconstruct images
"""
import cv2
import numpy as np

img = cv2.imread('lena.jpg')
lr = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr)
ur = cv2.pyrUp(lr2)
ur2 = cv2.pyrUp(ur)
cv2.imshow('Original Image', img)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('Upper Level Gauss Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    # Line gives the expanded version of its upper level in the
    # Gaussian Pyramid
    gaussExtended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussExtended)
    cv2.imshow(str(i), laplacian)
    # The output just looks like edge detection
cv2.waitKey(0)
cv2.destroyAllWindows()