import cv2

# Reading Image - flag (0, 1, -1)
img = cv2.imread('lena.jpg', 0)
print(img)

# Showing Image in Window
cv2.imshow('Lena', img)

# Wait for 5 seconds
cv2.waitKey(5000)

# Destroy all open windows
cv2.destroyAllWindows()

# Writing to file
cv2.imwrite('lena_again.png', img)

