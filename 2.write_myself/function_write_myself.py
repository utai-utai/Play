import pyautogui


def type(word):
    pyautogui.typewrite(word, interval=0.1)


def enter():
    pyautogui.press('enter')


def copy():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'v')
    enter()
    pyautogui.hotkey('ctrl', 'v')
    enter()
    pyautogui.hotkey('ctrl', 'v')


def write_function():
    type('im')
    enter()
    type('pya')
    enter()
    enter()
    type('fr')
    enter()
    type('fun')
    enter()
    type(' im')
    enter()
    type('w')
    enter()
    enter()
    enter()
    type('width, length = py')
    enter()
    type('.si')
    enter()
    enter()
    type('x, y = width / 2, length / 2 - 200')
    enter()
    type('pya')
    enter()
    type('.cl')
    enter()
    type('(x, y)')
    enter()
    type('pya')
    enter()
    type('.hot')
    enter()
    type("('ctrl', 'a')")
    enter()
    type('pya')
    enter()
    type('.hot')
    enter()
    type("('ctrl', 'x')")
    enter()
    type('wri')
    enter()
    enter()
    type('pya')
    enter()
    type('.cl')
    enter()
    type("(x, y, button='right')")
    copy()
    enter()
    pyautogui.hotkey('ctrl', '/')
    type('Little problem!')
    enter()
    type('for i in range(10):')
    enter()
    type("py")
    enter()
    type('.pr')
    enter()
    type('("down")')
    enter()
    pyautogui.press('backspace')
    type('for i in range(2):')
    enter()
    type("py")
    enter()
    type('.pr')
    enter()
    type('("enter")')
    enter()


def yanggu():
    pyautogui.typewrite('import random\n\nnum = 20\nx = [0 for x in range(num)]\nend = 0\nwhile True:\nfor i in range(len(x)):\nif ran', interval=0.25)
    pyautogui.press('tab')
    pyautogui.typewrite('.randi', interval=0.25)
    pyautogui.press('tab')
    pyautogui.typewrite('0, 2) == 1:\nx[i] += int(ran', interval=0.25)
    pyautogui.press('tab')
    pyautogui.typewrite('.rando', interval=0.25)
    pyautogui.press('tab')
    pyautogui.typewrite(' % 1 * 100)\n', interval=0.25)
    pyautogui.press('backspace')
    pyautogui.typewrite('if x[i] >= 1000:\nprint(str(i + 1) + " win")\nend = 1\n', interval=0.25)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite('if end == 1:\nbreak\n\n', interval=0.25)
    pyautogui.press('backspace')
    pyautogui.typewrite('print(x)', interval=0.25)