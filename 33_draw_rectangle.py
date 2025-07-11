import numpy as np
import cv2

h, w = map(int, input("Enter height and width: ").split())
img = 255 * np.ones((h, w, 3), np.uint8)

cv2.rectangle(img, (50, 50), (w-50, h-50), (0, 0, 255), 3)

cv2.imshow('Rectangle Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()