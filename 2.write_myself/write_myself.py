import pyautogui
from function_write_myself import write_function

width, length = pyautogui.size()
x, y = width / 2, length / 2 - 200
pyautogui.click(x, y)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')
write_function()
pyautogui.click(x, y, button='right')
pyautogui.click(x, y, button='right')
pyautogui.click(x, y, button='right')
# Little problem!
for i in range(10):
    pyautogui.press("down")
for i in range(2):
    pyautogui.press("enter")
