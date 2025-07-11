import cv2

# Read image
img = cv2.imread('sample.jpg')

# Rotate 90 degrees clockwise around y-axis (flip + transpose)
rotated = cv2.transpose(img)
rotated = cv2.flip(rotated, 1)

# Display
cv2.imshow('Original', img)
cv2.imshow('Rotated 90° Y-axis', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()