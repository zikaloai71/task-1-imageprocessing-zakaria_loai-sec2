import numpy as np
import cv2 as cv

img = cv.imread('sozy.jpeg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('new.jpg',res)

