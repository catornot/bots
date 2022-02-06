import pyautogui
import pydirectinput
import keyboard
import time 
from PIL import ImageGrab
import numpy as np
import cv2

time.sleep(1)

#pydirectinput.keyUp("w")
class bot:
    def __init__(self): 
        self.found_building = False

        # self.lower_range_building = np.array([20, 50, 70])
        # self.upper_range_building = np.array([60, 100, 120])
        self.lower_range_building = np.array([20,20,20])
        self.upper_range_building = np.array([30, 255, 255])

        self.screenshot_time = time.time()

    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def timer(self):
        # while keyboard.is_pressed('q') == False:
        # if(time.time() > self.screenshot_time + 0.4):
        self.screenshot_time = time.time()
        self.detect_color()

    def detect_color(self):
        im1 = pyautogui.screenshot("currentImg.png")
        im1 = cv2.imread("currentImg.png")
        hsv = cv2.cvtColor(cv2.UMat(im1), cv2.COLOR_BGR2HSV)
        mask_building = cv2.inRange(hsv, self.lower_range_building, self.upper_range_building)

        cv2.imwrite("HSV.png", hsv)
        cv2.imwrite("CurrentMaskBuilding.png", mask_building)
        print("yellow pixels: " + str(cv2.countNonZero(mask_building)))

        if(int(cv2.countNonZero(mask_building)) > 5000):
            release_inputs()
            print("Found buildings")

    def release_inputs(self):
        pydirectinput.keyUp("w")
        pydirectinput.mouseUp()
Bot = bot()   
Bot.timer()
# pydirectinput.keyUp("c")