import cv2
import numpy as np

img = cv2.imread('sample.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Perspective Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()