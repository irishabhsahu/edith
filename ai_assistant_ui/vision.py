import cv2 as cv
from ultralytics import YOLO
import numpy as np
import speech
from command import parse_command
command_text = ""

speech.start_listening()

model = YOLO("yolov8n.pt")

def find_workingCam(max_index=5):
    for index in range(max_index):
        cap=cv.VideoCapture(index, cv.CAP_ANY)
        if cap.isOpened():
            cap.release()
            return index
    return None
cam_index=find_workingCam()
if cam_index is None:
    print("No webcam found.")
    exit()
else:
    cap = cv.VideoCapture(cam_index, cv.CAP_ANY)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break
    frame=cv.resize(frame, (1920,1060))
    text_box=np.zeros((100, 1920, 3), dtype='uint8')
    cv.putText(text_box, speech.display_text, (30, 60), cv.FONT_HERSHEY_SIMPLEX, 1.0, speech.display_color, thickness=2)

    results = model(frame)
    annotated_frame = results[0].plot()

    command = parse_command(speech.transcribed_text)
    if command:
        command_text=f'Command: {command}'
        if command=="exit":
            break

    full_frame = np.vstack((annotated_frame, text_box))
    display_frame = cv.resize(full_frame, (1280, 720))
    cv.imshow("webcam", display_frame)

    if (cv.waitKey(1) & 0xFF) in [100, 27]:
        break

cap.release()
cv.destroyAllWindows()