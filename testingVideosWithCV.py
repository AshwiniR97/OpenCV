import cv2

# Using 0 argument as default to capture from camera
# If multiple cameras, test with 1, 2, -1
# Adding CAP_DSHOW to remove async callback error
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Getting FourCC code
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Opening VideoWriter Class to write - Arguments are filename, fourcc code, frames per second, (height, width))
out = cv2.VideoWriter('outputVideo.avi', fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()

    if(ret):
#       Printing Width and Height
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        print("\nFrame width is %f and height is %f", height, width)
#       To write frame to output file
        out.write(frame)
#       If you want to change the frame colouring
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video', gray)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
