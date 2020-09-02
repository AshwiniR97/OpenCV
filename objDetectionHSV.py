"""
HSV
Hue: Base Colour Pigment (0-360)
Saturation: Depth of pigment (0-100%)
Value: Brightness of colour (0-1)

Using HSV values to detect certain colours. In smarties.png there
are a variety of balls of different colours and we will try to filter out
specific coloured balls.
"""

import cv2
import numpy as np


def nothing(x):
    pass

# Video capture
cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Tracking", 255, 255, nothing)
while True:
    # frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold for blue, find lower and upper bounds
    lowerHue = cv2.getTrackbarPos("Lower Hue", "Tracking")
    lowerSat = cv2.getTrackbarPos("Lower Saturation", "Tracking")
    lowerVal = cv2.getTrackbarPos("Lower Value", "Tracking")

    upperHue = cv2.getTrackbarPos("Upper Hue", "Tracking")
    upperSat = cv2.getTrackbarPos("Upper Saturation", "Tracking")
    upperVal = cv2.getTrackbarPos("Upper Value", "Tracking")

    low = np.array([lowerHue, lowerSat, lowerVal])
    up = np.array([upperHue, upperSat, upperVal])
    mask = cv2.inRange(hsv, low, up)

    # Bitwise AND to mask the original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
