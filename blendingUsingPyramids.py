"""
Right of orange + Left of apple
Blending has 5 steps:
1. Load the two images
2. Find Gaussian Pyramid for apple and orange (Here no. of levels is 6)
3. Subsequently find Laplacian Pyramid
4. Join left half of apple and right half of orange in each level of Laplacian Pyramid
5. From joint image reconstruct orig image
"""
import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)

# Half and half stack
appleOrangeStack = np.hstack((apple[:, :256], orange[:, 256:]))

# Gaussian Pyramid - Apple
appleCopy = apple.copy()
gpApple = [appleCopy]

for i in range(6):
    appleCopy = cv2.pyrDown(appleCopy)
    gpApple.append(appleCopy)

# Gaussian Pyramid - Orange
orangeCopy = orange.copy()
gpOrange = [orangeCopy]

for i in range(6):
    orangeCopy = cv2.pyrDown(orangeCopy)
    gpOrange.append(orangeCopy)

# Laplacian Pyramid - Apple
appleCopy = gpApple[5]
lpApple = [appleCopy]

for i in range(5, 0, -1):
    gaussExt = cv2.pyrUp(gpApple[i])
    laplacian = cv2.subtract(gpApple[i - 1], gaussExt)
    lpApple.append(laplacian)

# Laplacian Pyramid - Orange
orangeCopy = gpOrange[5]
lpOrange = [orangeCopy]

for i in range(5, 0, -1):
    gaussExt = cv2.pyrUp(gpOrange[i])
    laplacian = cv2.subtract(gpOrange[i - 1], gaussExt)
    lpOrange.append(laplacian)

# Join halves of both laplacians
appleOrangeStack2 = []
for appleLap, orangeLap in zip(lpApple, lpOrange):
    # Shape of apple image
    cols, rows, ch = appleLap.shape
    laplacian = np.hstack((appleLap[:, 0:int(cols / 2)], orangeLap[:, int(cols / 2):]))
    appleOrangeStack2.append(laplacian)

# Reconstruct
appleOrangeRecon = appleOrangeStack2[0]

for i in range(1, 6):
    appleOrangeRecon = cv2.pyrUp(appleOrangeRecon)
    appleOrangeRecon = cv2.add(appleOrangeStack2[i], appleOrangeRecon)

# Output
cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("Half and Half", appleOrangeStack)
cv2.imshow("Reconstruct", appleOrangeRecon)
cv2.waitKey(0)
cv2.destroyAllWindows()
