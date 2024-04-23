# passo a passo do projeto



# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press

# passo 1 - entrar no sistema fictício https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import subprocess
import pandas

pyautogui.PAUSE = 1.30
# Aguarde alguns segundos antes de iniciar a automação

# Execute o comando para abrir o navegador 
subprocess.run(['google-chrome'])

time.sleep(1)

linkPonto = "servicos.solis"

pyautogui.write(linkPonto)

pyautogui.sleep(4)

# Pressione Enter para abrir o Chrome
pyautogui.press('enter')

pyautogui.doubleClick(x=982, y=406)

pyautogui.doubleClick(x=1055, y=678)

pyautogui.hotkey("ctrl", "t")

pyautogui.write("zimbra.s")

pyautogui.press("enter")

pyautogui.write("thais")

pyautogui.press("tab")

pyautogui.press("capslock")

pyautogui.write("a")

pyautogui.press("capslock")

pyautogui.write("marelo13+")

pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")

linkWhats = "web.whats"

pyautogui.write(linkWhats)

pyautogui.press("enter")



# passo 2 - fazer login no sistema
# passo 3 - importar a base de dados em csv
# passo 4 - cadastrar um produto
# passo 5 - repetir o cadastro até acabar os itens da base de dados