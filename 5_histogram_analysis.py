import cv2
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('sample.jpg')

# Plot histogram for each color channel
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.title('Color Histogram')
plt.show()