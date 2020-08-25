import numpy as np
import cv2

img = cv2.imread('lena.jpg')

# Overwrite Image
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 4)
img = cv2.circle(img, (255, 255), 50, (0, 255, 0), 4)
img = cv2.arrowedLine(img, (255, 255), (255, 0), (0, 0, 255), 3)

# Adding -1 as thickness will fill the shape with the colour
img = cv2.rectangle(img, (255, 255), (500, 500), (96, 117, 242), -1)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'OpenCV', (50, 255), font, 2, (60, 60, 60), 5, cv2.LINE_AA)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()