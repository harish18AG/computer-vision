import cv2

# Read image
img = cv2.imread('sample.jpg')
edges = cv2.Canny(img, 100, 200)

# Display
cv2.imshow('Original', img)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()