import pyautogui as p 

voltar = 'fotos/voltar.png'
jade = 'fotos/nomeJadePicon.png'
confirm = 'fotos/confirm.png'
atualizar = 'fotos/atualizar.png'
count = 0
def AlteraTela():
    p.keyDown('alt')
    p.press('tab')
    p.keyUp('alt')

def Localiza(nomeFoto):
    global count
    for localiza in p.locateAllOnScreen(nomeFoto):
        p.click((localiza.width+localiza.left) - localiza.width/2, (localiza.top+localiza.height)-localiza.height/2)
        if(nomeFoto =='fotos/voltar.png'):
            count+=1
            print(count)

while(True):
    Localiza(jade)
    Localiza(confirm)
    Localiza(voltar)  
    for att in p.locateAllOnScreen(atualizar):
        p.click(att.left, att.top-5)
        p.press('F5')
        p.sleep(0.5)

