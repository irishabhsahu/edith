import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow('Camera Test', frame)
    if cv.waitKey(0) == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
