import pyautogui
from PIL import Image
from pytesseract import *
import win32api, win32con
import win32clipboard
import webbrowser
import keyboard
from time import sleep
import pickle

print("press q when done")
sleep(2)
print("Ready")
sleep(0.5)
do = input("what to do :")
name = input("enter the name of the location :")
sleep(0.5)
print("waiting for the location")
location = {}
if "add" == do:
    with open("positions.txt","rb") as f:
        location = pickle.load(f)


while keyboard.is_pressed('q') == False:
    if win32api.GetKeyState(0x01) < 0:
        location[name] = tuple(pyautogui.position())
        print(f"location {location[name]}")
        sleep(0.5)
        name = input("enter the name of the next location :")
        sleep(0.5)
        print("waiting for next location")

print(location)

if input("do you want to save press anything but not no:") != "no":
    with open("positions.txt","wb") as f:
        pickle.dump(location,f)
        # print(pickle.load(f))