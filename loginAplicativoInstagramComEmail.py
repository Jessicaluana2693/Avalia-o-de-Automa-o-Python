# Questão 2. Objetivo: 
# Desenvolva um script em Python, que tem como objetivo realizar o login no aplicativo “Instagram”, utilizando uma conta de email.
import webbrowser
import pyautogui
import time

webbrowser.open('https://www.instagram.com/')

#Campo email
time.sleep(3)
pyautogui.click(x=1114, y=384, interval=0.25) 
pyautogui.write('teste@teste.com', interval=0.25)
pyautogui.press('tab')

#Campo senha
time.sleep(3)
pyautogui.click(x=1100, y=440, interval=0.25) 
pyautogui.write('seuasenhaaqui', interval=0.25)

#Clicar no botão Entrar
pyautogui.click(x=1198, y=495, interval=0.25) 

# OBS: por favor troque
# o email teste pelo seu email de preferência
# a senha testes por sua senha de usuário
# obrigada :)