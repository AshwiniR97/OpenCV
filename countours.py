"""
Curve joining all continuous points along the boundary which have same colour/intensity
CV_RETR_EXTERNAL only gives outer contours, if you get enclosing ones the outermost is given
CV_RETR_LIST gives all the contours regardless of nested or not
CV_RETR_CCOMP organizes into inner or outer contour + hierarchy variable is adjusted accordingly - useful to find holes
CV_RETR_TREE full hierarchy of contours
"""
import cv2

imgOrig = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# contours - all the contours in an image, has a list of points that form rectange to draw boundary on image
# heirarchy - topological data
contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours: ", str(len(contours)))

# Third argument -1, will draw all contours, else draw the indexed contour
cv2.drawContours(imgOrig, contours, 7, (0, 255, 0), 2)
cv2.imshow("Gray Image", img)
cv2.imshow("Contours", imgOrig)
cv2.waitKey(0)
cv2.destroyAllWindows()