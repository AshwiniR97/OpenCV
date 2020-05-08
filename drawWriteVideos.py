import cv2
import numpy as np
import datetime

# Using 0 argument as default to capture from camera
# If multiple cameras, test with 1, 2, -1
# Adding CAP_DSHOW to remove async callback error
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# To know height and width of video
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# To set height and width of video (set as per resolution of camera)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

# Getting FourCC code
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Opening VideoWriter Class to write - Arguments are filename, fourcc code, frames per second, (width, height))
out = cv2.VideoWriter('outputVideo.avi', fourcc, 20.0, (1280, 720))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Printing Width and Height
        # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        # textToWrite = "Height: " + str(height) + " Width: " + str(width)

        dateAndTime = str(datetime.datetime.now())

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, dateAndTime, (0, 20), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

        # To write frame to output file
        out.write(frame)

        # If you want to change the frame colouring
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
