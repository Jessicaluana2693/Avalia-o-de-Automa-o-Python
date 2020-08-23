# Questão 1. Objetivo: script em Python, que tem como objetivo realizar o download de um aplicativo na PlayStore.
import webbrowser
import pyautogui
import time

# abre o site do play store
webbrowser.open('https://play.google.com/store?hl=pt_BR')

# move o cursos para o campo de busca e clica no campo
time.sleep(4)
pyautogui.moveTo(616, 165, duration=0.25)
pyautogui.click(616, 165, button='left', duration=0.25)

# preenche o campo de busca com Instagram e pressiona Enter
pyautogui.write('Instagram', interval=0.25)
pyautogui.press('enter')

# o cursos é movido até o primeiro campo e é clicado o icone do instagram
time.sleep(3)
pyautogui.moveTo(383, 604, duration=0.25)
pyautogui.click(383, 604, button='left', duration=0.25)

# o usuário é redirecionado a página de detalhe e é clicado o botão INSTALAR
time.sleep(4)
pyautogui.click(x=1186, y=558, interval=0.25) 

# um modal é aberto para confirmar o aparelho e é clicado no botão CONTINUAR
time.sleep(4)
pyautogui.click(x=1087, y=705, interval=0.28)

# o usuário é redirecionado a sua conta google para verificar sua autenticidade e é clicado o botão PROXIMA
time.sleep(3)
pyautogui.click(x=1119, y=625, interval=0.25) 

# o usuário precisa confirmar que realmente é dono da conta google
# por motivos didaticos eu coloquei um alert pedindo que o usuário coloque sua senha para confirmação
pyautogui.click(x=839, y=592, interval=0.25) 
okpressed = pyautogui.alert(text='Aqui você coloca sua senha para confirmar a instalação', title='senha para confirmação',button='OK')
if(okpressed=='OK'):
    time.sleep(7) # tempo para por a senha
    pyautogui.click(x=1129, y=711, interval=0.29) #clique no botãp PROXIMA

# após todo o processo um modal com uma mensagem de confirmação de instalação será enviado para o usuário
time.sleep(2)
pyautogui.click(x=1235, y=687, clicks=2, interval=0.25) #click no ok do modal

# INFORMAÇÕES IMPORTANTES
# os testes foram feitos numa tela de 15.6 polegadas Full-HD
# Tamanho em torno de: 1920 x 1080
#------------------------------------------
# os próximos passos complementares após a mensagem de alert são:
# 1. por a senha de usuário
# 2. após alguns segundos o sistema vai clicar no botão próxima
# 3. automaticamente volta para a tela de "detalhes" do aplicativo instagram na app store
# e clica no botão "ok" do pop que alerta que o app será instalado em alguns minutos no seu aparelho celular

# 4. automaticamente tbm o app é instalado no celular, para verificar é necessário apenas desbloquear seu celular e
# verificar em seu menu principal
# 5. Ou ver na tela de detalhe do instagram no play store o botão afirmando que o app foi instalado

#OBS:
# por motivos praticidade e facilidade eu irei finalizar essa automação voltando para tela de detalhe na playstore
# A qual mostra se o aplicativo esta instalado ou não.
# também resolvi mostrar um alert para informar o usuário que deve inserir sua senha para confirmar que realmente
# deseja fazer a instalação (segundo o passo a passo da própria play store no PC)




