import pyautogui, time
time.sleep(5)
f = open("Hier Textdatei aus deinem Ordner einfügen z.B. Beescript.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")