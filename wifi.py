import pyautogui
import time


# print(pyautogui.position())
# Point(x=1070, y=600)
# Point(x=280, y=610)
# Point(x=62, y=584)
# Point(x=50, y=576)

def off():
    pyautogui.click(1070, 590)
    time.sleep(5)
    pyautogui.click(280, 610)


def on():
    pyautogui.click(1070, 599)
    time.sleep(5)
    pyautogui.click(62, 584)
    time.sleep(1)
    pyautogui.click(50, 576)
