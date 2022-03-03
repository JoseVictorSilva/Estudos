import pyautogui as p 

voltar = 'fotos/voltar.png'
barbara = 'fotos/barbaraNome.png'
confirm = 'fotos/confirm.png'
def AlteraTela():
    p.keyDown('alt')
    p.press('tab')
    p.keyUp('alt')

def Localiza(nomeFoto):
    if(p.locateOnScreen(nomeFoto,confidence = 0.8)):
        return True
    
def IdentficaVolta():
    if(Localiza(voltar)):
        print('apareceu')
        return True
AlteraTela()

p.PAUSE = 0.8
n = 0
p.click(100,100)
while(True):
    if(Localiza(barbara)):
        p.click(barbara)
    if(Localiza(confirm)):
        p.click(confirm)
        n+=1
    if(Localiza('fotos/pular.png')):
        pular = p.locateCenterOnScreen('fotos/pular.png')
        p.click(pular[0]+80,pular[1])
        p.press('F5')
    if(Localiza(voltar)):
        p.click(voltar)

