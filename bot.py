import pyautogui, time
""" pyautogui is an automation gui that does any work without user intervention """

time.sleep(5)  # so that the program doesn't starts spamming instantly
f = open('script.txt', 'r') # opening the script to spam
for lines in f:
    pyautogui.typewrite(lines)
    pyautogui.press('enter')