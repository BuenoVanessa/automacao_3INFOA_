import pyautogui, pyscreeze

#localiza x, y de uma imagem na tela 
nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png', confidence=.9)
pyautogui.click(nome_XY, duration=0.5)#Clica 
pyautogui.write('Vanessa Bueno')

campo_cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png', confidence=.9)
pyautogui.click(campo_cpf_XY, duration=0.5)#Clica 
pyautogui.write('139.500.016-62')

campo_sim_XY = pyautogui.locateCenterOnScreen('./semana7/campo_sim.png', confidence=.9)
pyautogui.click(campo_sim_XY, duration=0.5)#Clica 
