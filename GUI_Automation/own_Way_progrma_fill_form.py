# "Automate the Boring Stuff" book/
# CH18: Automatic Form filler - Form x2 version.
# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

import pyautogui,time

print('How many forms you want to fill?')
number = input()
time.sleep(5)

for i in range(int(number)):   
    pyautogui.doubleClick(328, 391)
    pyautogui.typewrite('Daniel Ramirez')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('Heights')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite(['down','down','down'])
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite(['right','right','right','right'])
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('Back to the future was the greatest action movie in the 1980s')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite(['enter'])
    time.sleep(2)
    pyautogui.click(449, 286)
    time.sleep(2)
   
