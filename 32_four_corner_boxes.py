import numpy as np
import cv2

h, w = map(int, input("Enter height and width: ").split())
img = 255 * np.ones((h, w, 3), np.uint8)
box_h, box_w = h // 10, w // 10

img[0:box_h, 0:box_w] = [0, 0, 0]        # Black
img[0:box_h, -box_w:] = [255, 0, 0]      # Blue
img[-box_h:, 0:box_w] = [0, 255, 0]      # Green
img[-box_h:, -box_w:] = [0, 0, 255]      # Red

cv2.imshow('Image with Colored Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()