import pyautogui
import pydirectinput
import time

## vars
hakiFull = [85, 85, 255]

HakiEmpty = [52, 52, 158]

hakiLocX = 1099
hakiLocY = 904

for y in range(0, 1080):
    for x in range(0, 1920):
        time.sleep(4)
        print(pyautogui.pixel(hakiLocX, hakiLocY))
        currPix = pyautogui.pixel(hakiLocX, hakiLocY)
        for RGB in hakiFull:
            if RGB == currPix[2]:
                pydirectinput.keyDown('j')
                time.sleep(0.1)
                pydirectinput.keyUp('j')
            else:
                pass
