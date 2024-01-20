import cv2 
import numpy as np
import pyautogui

SCREENSIZE = (1920,1080) #SCEEN SIZE

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("NameVideo.mp4", fourcc, 20.0, (SCREENSIZE))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('screenshot', frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()
out.release()