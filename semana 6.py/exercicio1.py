#Fazer uma pesquisa no google 
#Clique no campo de pesquisa, após digite o texto 'como automatizar o whatsapp após precione a tecla enter 
import pyautogui
pyautogui.click(370, 393, duration=0.5)
pyautogui.write('Como automatizar o whatssap')
pyautogui.press("enter")

pyautogui.click(32,442, duration=0.2)
pyautogui.dragTo(34,577, duration=0.2)
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(1208,354)
pyautogui.hotkey('ctrl', 'v')