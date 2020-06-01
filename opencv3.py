import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)
img= np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,255), (255,0), (255,34,56), 5)
img = cv2.rectangle(img, (304,0), (458,265), (255,0,255), 5)
img = cv2.circle(img, (304,265), 45, (0,67,93), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Aryan', (10,500), font, 2, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()