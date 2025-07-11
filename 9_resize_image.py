import cv2

# Read image
img = cv2.imread('sample.jpg')

# Resize smaller and bigger
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
big = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)

# Display
cv2.imshow('Original', img)
cv2.imshow('Small', small)
cv2.imshow('Big', big)
cv2.waitKey(0)
cv2.destroyAllWindows()