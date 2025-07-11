import cv2

img = cv2.imread('sample.jpg')
text = input("Enter the text to display: ")
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, text, (50, 50), font, 1, (0, 255, 255), 2)

cv2.imshow('Image with Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()