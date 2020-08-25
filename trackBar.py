import numpy as np
import cv2


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Image')

# Trackbar to change the Blue channel value of the image
cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('R', 'Image', 0, 255, nothing)

switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

boolVal = True

while True:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get trackbar position of each of them
    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')

    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0 and boolVal is True:
        img = cv2.bitwise_not(img)
        boolVal = False
    else:
        # Setting Image colour based on trackbar positon
        img[:] = [b, g, r]
cv2.destroyAllWindows()
