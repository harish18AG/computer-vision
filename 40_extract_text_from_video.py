import cv2
import pytesseract

cap = cv2.VideoCapture('sample_video.mp4')
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame_count > 50:  # Process only first 50 frames
        break
    text = pytesseract.image_to_string(frame)
    print(f"Frame {frame_count}:
{text}
")
    frame_count += 1

cap.release()