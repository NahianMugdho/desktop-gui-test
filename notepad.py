# used to access time related functions
import time
import pyautogui

# pauses the execution of the program
# for 5 sec
time.sleep(5)
pyautogui.moveTo(1415,1059, duration = 1)
pyautogui.click()
# types the string passed inside the
# function
pyautogui.typewrite("Geeks For Geeks!")