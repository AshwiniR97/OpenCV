"""
Multi stage algo
1. Gaussian Filter noise red
2. Gradient Calculation (Intensity Gradients)
3. Non-maximum suppression to get rid of spurious reactions to edge detection
4. Double threshold to determine potential edges
5. Track edges by hysteresis - suppressing weaker edges
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass


cv2.namedWindow('Threshold')
cv2.createTrackbar("Thres1", "Threshold", 0, 255, nothing)
cv2.createTrackbar("Thres2", "Threshold", 200, 255, nothing)

img = cv2.imread('sudoku.png', 0)
# Add trackbar for thres1 and thres2

while True:
    thres1 = cv2.getTrackbarPos("Thres1", "Threshold")
    thres2 = cv2.getTrackbarPos("Thres2", "Threshold")
    print(thres1, thres2)
    canny = cv2.Canny(img, thres1, thres2)
    titles = ['image', 'Canny']
    images = [img, canny]

    for i in range(len(images)):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        # xticks and yticks will add/remove axes
        plt.xticks([])
        plt.yticks([])

    plt.show()

cv2.destroyAllWindows()