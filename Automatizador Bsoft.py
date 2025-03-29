import pyautogui
from time import sleep

#1 - Abrir o Google   
pyautogui.click(702,1056, duration = 1)
sleep(2)
#2 - Digitar na barra de pesquisa e dar enter
pyautogui.click(294,61, duration = 1)
pyautogui.write('https://sis.bsoft.com.br/')
pyautogui.press('enter')
#3 - Digitar TAG   
pyautogui.click(1227,463, duration = 1)
pyautogui.write('')
#4 - Confirmar TAG
pyautogui.click(1401,458, duration = 1)
#5 - Entrar na próxima tela
pyautogui.click(1185,580, duration = 1)
#6 - Digitar usuário
sleep(18)
pyautogui.click(1154,523, duration = 1)
pyautogui.write('')
#7 - Digitar senha  
pyautogui.click(1156,566, duration = 4)
pyautogui.write('')
#8 - Entrar no Bsoft
pyautogui.click(1362,602, duration = 1)
