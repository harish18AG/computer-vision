import cv2

img = cv2.imread('sample.jpg')
overlay = img.copy()
watermark = "SRIKESH"

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(overlay, watermark, (50, 50), font, 1, (0, 255, 0), 2)

cv2.imshow('Original', img)
cv2.imshow('Watermarked', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()