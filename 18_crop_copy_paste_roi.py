import cv2

img = cv2.imread('sample.jpg')
roi = img[50:150, 50:150]  # Crop a region
img[200:300, 200:300] = roi  # Paste it elsewhere

cv2.imshow('Modified Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()