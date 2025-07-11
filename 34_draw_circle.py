import numpy as np
import cv2

h, w = map(int, input("Enter height and width: ").split())
img = 255 * np.ones((h, w, 3), np.uint8)

center = (w // 2, h // 2)
radius = min(w, h) // 4
cv2.circle(img, center, radius, (0, 255, 0), 3)

cv2.imshow('Circle Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()