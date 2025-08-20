import pyautogui

# cursor moves to a specific position
pyautogui.moveTo(1184,1075, duration = 1)

# left clicks at the current position
pyautogui.click()

# cursor moves to a specific position
pyautogui.moveTo(1284,150, duration = 1)

# left clicks and holds and moves the
# cursor to (500,500) position
pyautogui.dragTo(1399,450, duration = 1)

# drags the cursor relative to it's
# position to 5opx right and 50 px down
pyautogui.dragRel(50,50, duration=1)