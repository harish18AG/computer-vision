import cv2

cap = cv2.VideoCapture('sample_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Slow Motion
    cv2.imshow('Slow Motion', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cap = cv2.VideoCapture('sample_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Fast Motion
    cv2.imshow('Fast Motion', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()