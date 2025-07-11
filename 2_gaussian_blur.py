import cv2

# Read image
img = cv2.imread('sample.jpg')
blurred = cv2.GaussianBlur(img, (15, 15), 0)

# Display
cv2.imshow('Original', img)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()