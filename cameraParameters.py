# Repeat of another lesson
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Use ca.set() to set values to properties
# Associated property number can be found by selecting the value and the prop will show
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)

        if ord('q') == cv2.waitKey(1) & 0xFF:
            break
        else:
            # Even if you close the window it'll keep coming up
            continue

cap.release()
cv2.destroyAllWindows()
