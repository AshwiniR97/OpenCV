"""
Draw bounding boxes around moving objects and print status whether
movement is occuring in the screen or not
"""
import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Gets absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Blur the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Find threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Then we will dilate the thresholded image to fill in all the holes
    # Helps find better contours
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("Feed", frame1)
    frame1 = frame2
    # Reading two frames and finding the two frames
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
