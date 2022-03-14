import ctypes as c, time 


ok = c.windll.user32.BlockInput(True)
time.sleep(5)
ok = c.windll.user32.BlockInput(False)
print('Pronto')