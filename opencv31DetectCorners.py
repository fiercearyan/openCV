import numpy as np
import cv2 as cv

img = cv.imread("chessboard.png")

#cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.01)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst',img)

cv.waitKey(0)
#if cv.waitKey(1) & 0xFF == 27:
cv.destroyAllWindows()