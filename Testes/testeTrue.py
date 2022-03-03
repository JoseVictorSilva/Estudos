import pyautogui as p, time
time.sleep(2)
local = p.locateCenterOnScreen('fotos/confirm.png', confidence = 0.7)

p.click(local[0]+80, local[1])
p.scroll(-200) 
