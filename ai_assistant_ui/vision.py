import cv2 as cv
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Try different indexes if needed: 0, 1, etc.
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv.imshow("webcam", annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()