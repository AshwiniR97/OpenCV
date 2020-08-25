import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('image_1.png')

# Bitwise AND of images
bitAnd = cv2.bitwise_and(img2, img1)

# Bitwise OR of images
bitOr = cv2.bitwise_or(img1, img2)

# Bitwise Not of image
bitNot = cv2.bitwise_not(img1)

# Bitwise XOR of images
bitXor = cv2.bitwise_xor(img1, img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise And', bitAnd)
cv2.imshow('Bitwise Or', bitOr)
cv2.imshow('Bitwise Not', bitNot)
cv2.imshow('Bitwise Xor', bitXor)
cv2.waitKey(0)
cv2.destroyAllWindows()