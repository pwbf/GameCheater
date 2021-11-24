import numpy as np
import cv2
#For: https://www.arealme.com/reaction-test/zh/
from PIL import ImageGrab
import win32api, win32con
from time import time as timer

garray = np.array([0,244,117])
rarray = np.array([237,51,55])

clicked = False

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

while True:
    startA = timer()
    #start = timer()
    img = ImageGrab.grab(bbox=(400,600,600,700)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #print("TimeGrab: "+str(timer() - start))
    #start = timer()
    compR = img_np[0][0] == rarray
    compG = img_np[0][0] == garray
    #print("TimeComp: "+str(timer() - start))
    #start = timer()
    if(compR.all()):
        clicked = False
        print("Red")
    if(compG.all() and clicked == False):
        click(450,650)
        print("Green")
        print("TimeAll: "+str(timer() - startA))
        clicked = True
    #print("TimeDecide: "+str(timer() - start))
    #print("\n")
    
cv2.destroyAllWindows()