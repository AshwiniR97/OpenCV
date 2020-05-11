import cv2
import numpy as np

"""
# Prints all the classes and member functions inside cv2 package that contain 'EVENT' keyword in them
events = [i for i in dir(cv2) if 'EVENT' in i]

#['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 
'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 
'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
print(events)
"""


def clickEvent(event, x, y, flags, param):
    """
    :param event: Mouse Click Event
    :param x: X coordinate of click
    :param y: Y coordinate of click
    :param flags:
    :param param:
    :return:
    """

    if event == cv2.EVENT_LBUTTONDOWN:
        # The bgr you read, fill in another window
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        colourImage = np.zeros((512, 512, 3), np.uint8)
        colourImage[:] = [blue, green, red]
        cv2.imshow('Colour From Image', colourImage)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)
points = []

# Waits for mouse event and transfers to clickEvent()
cv2.setMouseCallback('Image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
