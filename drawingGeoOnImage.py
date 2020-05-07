import cv2

# If you want a coloured background
# Use img = _np.zeros([height, width, 3], np.uint8)
# Using zeros() will give a black background

img = cv2.imread('lena.jpg', 1)

# Putting A Line
img = cv2.line(img, (0, 0), (255, 255), (128, 0, 128), 5)

# Putting A Circle
img = cv2.circle(img, (128, 128), 10, 5)

# Putting a Rectangle
img = cv2.rectangle(img, (128, 128), (200, 200), (0, 128, 128), thickness=10)

# Putting an Arrowed Line
img = cv2.arrowedLine(img, (128, 128), (128, 0), (0, 0, 0), thickness=4)

# To inset text
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'This OpenCV', (0, 255), font, 2, (255, 0, 0), thickness=4)

cv2.imshow('Blah', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
