import time

import pyautogui

# cursor moves to a specific position
pyautogui.moveTo(1422,1054, duration = 1)

# left clicks at the current position
pyautogui.click()
time.sleep(10)
# cursor moves to a specific position
pyautogui.hotkey("ctrl","n")
time.sleep(5)
# left clicks and holds and moves the
# cursor to (500,500) position
pyautogui.typewrite("Geeks For Geeks!")
pyautogui.moveTo(1785,17, duration = 1)
pyautogui.click()
# drags the cursor relative to it's
# position to 5opx right and 50 px down
