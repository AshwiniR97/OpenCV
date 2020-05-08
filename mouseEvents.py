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
        # The coordinates will be printed wherever mouse event occured
        font = cv2.FONT_ITALIC
        strXY = "X: " + str(x) + " Y:" + str(y)
        print(strXY)
        cv2.putText(img, strXY, (x, y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('Image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Print the BGR channel values
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strColour = "B: " + str(blue) + " G: " + str(green) + " R: " + str(red)
        print(strColour)
        cv2.putText(img, strColour, (x, y), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('Image', img)


#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)

# Waits for mouse event and transfers to clickEvent()
cv2.setMouseCallback('Image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
