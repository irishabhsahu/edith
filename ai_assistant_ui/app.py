import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)

while True:
    ret, frame=capture.read()
    cv.imshow("Assistant", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    if not ret:
        break

capture.release()
cv.destroyAllWindows()