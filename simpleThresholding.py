import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)

# cv.THRES_BINARY is binary thresholding - either 0 or 1
# cv.THRESH_BINARY_INV binary thresholding but inverse - <127 gives 1 and >127 gives 0
# cv.THRESH_TRUNC - upto threshold value is not changed, beyond threshold value pixels are equated to threshold value
# cv.THRESH_TOZERO - pixel val < thres, pixel = 0, else unchanged from orig image
# cv.THRESH_TOZERO_INV - pixel val > thres, pixel = 0, else unchanged from orig image
# thres, pixel = 0, else unchanged from orig image
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

cv.imshow("Image", img)
cv.imshow("Thres", th1)
cv.waitKey(0)
cv.destroyAllWindows()