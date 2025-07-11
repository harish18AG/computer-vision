import cv2

img = cv2.imread('sample.jpg')
watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
watches = watch_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Watch Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()