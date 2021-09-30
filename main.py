import pyautogui
from PIL import Image
from pytesseract import *
import win32api, win32con
import win32clipboard
import webbrowser
import keyboard
from time import sleep
import pickle

sleep(2)
print("Ready")
sleep(0.5)
print("waiting for next location of the copy place")
# webbrowser.open("https://www.rulergame.net/new-english-ruler-game.php", new=2)
#https://www.rulergame.net/new-english-ruler-game.php
#Note: You have to change the path below to your tesseract.exe location



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def drag(pos1,pos2):
    win32api.SetCursorPos(pos1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.2) #This pauses the script for 0.1 seconds
    win32api.SetCursorPos(pos2)
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def getclip():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def get_inch(xy):
    click(xy[0],xy[1])
    click(xy[0],xy[1])
    click(xy[0],xy[1])
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

    return getclip().replace('"','')

pytesseract.tesseract_cmd = r'C:\\Users\\irina\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
def img_text(x1,y1,x2,y2):
    img = pyautogui.screenshot("bruh.png",region=(x1,y1,x2-x1,y2-y1))

    return pytesseract.image_to_string(img)

def locate_imgs(imgs):
    found = {}
    for img in imgs:
        box = pyautogui.locateCenterOnScreen(f"img/{img}.png",confidence=0.99)
        print(box, "yes")
        found[img] = list(box)
    return found

def locate_img(img):
    box = pyautogui.locateCenterOnScreen(f"img/{img}.png",confidence=0.86)
    print(box, "yes")
    return box

# location = []
# x = 0
# while keyboard.is_pressed('q') == False:
#     if win32api.GetKeyState(0x01) < 0:
#         location.append(tuple(pyautogui.position()))
#         print(f"location {location[x]}")
#         x += 1
#         sleep(0.5)
#         if x == 2:
#             break
#         print("waiting for next location")


print("starting in 1 second")
sleep(1)
print("started")

# y = (location[1][1] - location[0][1]) * 0.4 + location[0][1]
imgs = ["condensation","evaporation","groundwater","infiltration","lake","ocean","percolation",
"precipitation", "river","runoff","sublimation","transpiration"]

# locations = locate_imgs(imgs) 

with open("positions.txt","rb") as f:
        location_name = pickle.load(f)

while keyboard.is_pressed('q') == False:
    for name in imgs:
        l = locate_img(name)
        sleep(0.1)
        drag(l, location_name[name])
    sleep(0.001)
    break
click(1364, 724)
print("end")


     # text = get_inch(location_of_text[0])
    # text = img_text(location[0][0],location[0][1],location[1][0],location[1][1])
    # print(text)
    # print(eval(f"{location[1][0]-location[0][0]} * ({text})"))

    # place = int(eval(f"{location[1][0]-location[0][0]} * ({text})") + location[0][0])
    # click(place,int(y))