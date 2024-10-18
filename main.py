import pyautogui
import time

def toggle_locks_off():
    for lock in ('scrolllock', 'capslock', 'numlock'):
        pyautogui.press(lock)

def count():
    pyautogui.press('scrolllock')

    for count in range(1, 9):
        pyautogui.press('scrolllock')

        if count % 2 == 1 and count >= 2:
            pyautogui.press('capslock')
        if count == 5:
            pyautogui.press('numlock')
        if count == 8:
            time.sleep(1)
            toggle_locks_off()
        else:
            time.sleep(0.9)


for _ in range(10):
    count()
