import pyautogui
import time

# U can change the value of this integer.
spam_amount = 100

# Makes sure this program waits 5 seconds
# before starting so u have enough time to open for example the chat u want to spam in.
# U can change this value aswell
time.sleep(5)

for i in range(spam_amount):
    f = open('text', 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")