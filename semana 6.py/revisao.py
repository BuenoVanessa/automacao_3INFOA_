import pyautogui

#movimentar o mouse 
pyautogui.moveTo(960, 540, duration=.5)
pyautogui.moveRel(100, 100)

#Movimneto de arrastar
pyautogui.dragTo(960,540, duration=.5)
pyautogui.dragRel(100,100, duration=.5)

#Clicar
pyautogui.click(960,540, clicks=2, button='RIGHT')

#Rolagem 
pyautogui.scroll(-2)

#Pra subir positivo e pra descer negativo 
#Teclado
#Escrever 
pyautogui.write('olá')

#Precionar uma tecla especifica
pyautogui.press("enter")

#Precionar teclas simultaneas 
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

#Manter as teclas precionadas 
pyautogui.keyDown('a')
pyautogui.keyUp('a')