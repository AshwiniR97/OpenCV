import cv2

# Reading Image - flag (0, 1, -1)
img = cv2.imread('lena.jpg', 0)

cv2.imshow('WinName', img)

k = cv2.waitKey(0)
print("Value of k: ", k)

if k == ord('s'):
    cv2.imwrite('newLena.png', img)
    print("Entered This Loop")
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()