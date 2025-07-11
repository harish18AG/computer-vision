import cv2
import numpy as np

# Read image
img = cv2.imread('sample.jpg')
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(img, kernel, iterations=1)

# Display
cv2.imshow('Original', img)
cv2.imshow('Dilated', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()