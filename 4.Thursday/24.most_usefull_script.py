# pip install pyautogui

import pyautogui
import time
import random

screen_width, screen_height = pyautogui.size()
print("wit:", screen_width, "Height: ", screen_height)

while True:
    seconds = random.randint(1,3)
    print(f"sleepin for {seconds}")
    time.sleep(seconds)
    x_random = random.randint(0, screen_width)
    y_random = random.randint(0, screen_height)
    pyautogui.moveTo(x_random, y_random, duration=1,)

    
