import cv2

img = cv2.imread('sample.jpg')
rotated = cv2.transpose(img)
rotated = cv2.flip(rotated, 0)  # Flip vertically after transpose

cv2.imshow('Original', img)
cv2.imshow('270 Degree Y-Axis Rotation', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()