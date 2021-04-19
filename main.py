# This code is written by Rajdeep Majumder (@razrexe)
# watch my video tutorial and follow along this for help and try to code this on your own. Have fun and stay curious!!
import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x , y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # uncomment this part with winsound if you need to play the beeping sound when any movement is detected by the camera
        # winsound.Beep(500, 200)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('YoTiger Cam', frame1)