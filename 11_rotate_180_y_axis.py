import cv2

img = cv2.imread('sample.jpg')
rotated = cv2.flip(img, 1)  # Flip horizontally (180 degrees on Y-axis)

cv2.imshow('Original', img)
cv2.imshow('180 Degree Y-Axis Rotation', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()