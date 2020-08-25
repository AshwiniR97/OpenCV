import cv2
import numpy as np



# Using 0 argument as default to capture from camera
# If multiple cameras, test with 1, 2, -1
# Adding CAP_DSHOW to remove async callback error
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Getting FourCC code
fourCC = cv2.VideoWriter_fourcc(*'XVID')

# Opening VideoWriter Class to write - Arguments are filename, fourCC code, frames per second, (height, width))
out = cv2.VideoWriter('outputVideo.avi', fourCC, 20.0, (640, 480))

while True:
    ret, frame = cap.read()

    if ret:
        frame[0:180, :, :] = frame[300:600, :, :]
        # To write frame to output file
        out.write(frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
