import pyautogui as p

p.PAUSE = 0.01
p.keyDown('alt')
p.press('tab')
p.keyUp('alt')
n = 0
while(n<10000):
    p.click()
    n+=1
    