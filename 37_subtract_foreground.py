import cv2
import numpy as np

img = cv2.imread('sample.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 0])
upper = np.array([180, 255, 100])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Foreground Removed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()