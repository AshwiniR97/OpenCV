import cv2
import numpy as np

chessboard = cv2.imread('chessboard.png')
lena = cv2.imread('lena.jpg')

chessboard = cv2.resize(chessboard, (512, 512))
lena = cv2.resize(lena, (512, 512))

# dst = cv2.add(chessboard, lena)
# dst = cv2.add(lena, chessboard)
dst = cv2.addWeighted(lena, 0.1, chessboard, 0.1, 0)

cv2.imshow('Overlay', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
