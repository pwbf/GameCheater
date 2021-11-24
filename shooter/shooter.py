#For: https://www.arealme.com/aim-test/zh/
import cv2
import numpy as np
from PIL import ImageGrab
import win32api, win32con

tar = cv2.imread('target.png', 0)
#tar_gray = cv2.cvtColor(tar, cv2.COLOR_BGR2GRAY)
threshold = 0.95

scrcoord = [200,300,800,800]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

while True:
    img_rgb = np.array(ImageGrab.grab(bbox=(scrcoord[0],scrcoord[1],scrcoord[2],scrcoord[3]))) #x, y, w, h
    frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    frame_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(frame_gray,tar,cv2.TM_CCOEFF_NORMED)
    loc = list(np.where(res >= threshold))
    w, h = tar.shape[::-1]
    for pt in zip(*loc[::-1]):
        coord = [pt[0]+int(w/2), pt[1]+int(h/2)]
        click(scrcoord[0]+coord[0],scrcoord[1]+coord[1])
        print("X:"+str(scrcoord[0]+coord[0])+" Y:"+str(scrcoord[1]+coord[1]))
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
        cv2.circle(frame, (coord[0], coord[1]) , 2, (0,255,255), 1)
    print()
    cv2.imshow('Detected',frame)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()
