import cv2
import numpy as np

img = cv2.imread('sample.jpg')
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Black Hat Operation', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()