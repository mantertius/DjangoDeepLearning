import numpy as np
import cv2
# Load a video from file
capture = cv2.VideoCapture(0)
while True:
    # capture frame-by-frame from video file
    ret, frame = capture.read() 
    # show the frame on the screen
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()