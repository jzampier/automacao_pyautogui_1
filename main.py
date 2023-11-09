import pyautogui
from icecream import ic
from time import sleep

# res = pyautogui.locateOnScreen("img.png")
# ic(res)
# sc_x, sc_y = pyautogui.locateCenterOnScreen("img.png", confidence=0.9)
# engrenagem = pyautogui.locateOnScreen("engrenagem.png")
# ic(engrenagem)

# most important function locateCenterOnScreen("imagem.png") retorna a posição x,y do centro da imagem
# eng_x, eng_y = pyautogui.locateCenterOnScreen("engrenagem.png", confidence=0.9)
# ic(sc_x, sc_y)
# ic(eng_x, eng_y)
# pyautogui.moveTo(eng_x, eng_y)
# sleep(3)
# pyautogui.moveTo(sc_x, sc_y)

# pop-up para informar o Nome do canal
nome_canal: str = pyautogui.prompt(text='', title='Nome do canal')
ic(nome_canal)
# Open a new browser tab
pyautogui.hotkey('ctrl', 't')
sleep(2)
# Search on YouTube
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('https://www.youtube.com/')
pyautogui.hotkey('enter')
sleep(2)
# localizar o canal
x, y = pyautogui.locateCenterOnScreen('youtube_pesquisar.png', confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
pyautogui.write(nome_canal)
# pyautogui.hotkey('enter')
pyautogui.press('enter')

# click no canal
sleep(2)
x, y = pyautogui.locateCenterOnScreen('hash_logo.png', confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()
