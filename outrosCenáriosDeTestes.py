# Questão 3. objetivo: Descreva outros dois cenários de testes que podem ser aplicados ao “Instagram”

# para esta abordagem eu irei usar escrita de cenários de testes em formato de BDD

# 1.
#     Feature: Testando o campo senha com credenciais enválidas

#     Cenário: Campo senha não deve permitir espaços em branco
#         Quando acessamos a página de login do Instagram "https://www.instagram.com/"
#         E preenchemos o campo senha com 6 ou mais espaços em branco
#         E clicamos no botão "Entrar"
#         Então o sistema deve mostrar uma mensagem de erro informando que esse tipo de senha é inválida
# 2.
#     Feature: Preenchimento do "Esqueci a senha" com credenciais inválidas

#     Cenário: Campo de usuário deve apenas permitir formatos de celulares ou usuário válidos
#         Quando clicamos em esqueci a senha na página de login do Instagram
#         E somos redirecionados para a tela de Resetar senha
#         E preenchemos o campo de <usuário> com apenas espaços em branco
#         Então sistema deve enviar uma mensagem de erro informando que o usuário é inválido
#         E deixar o campo em branco novamente

#Exemplos de usuários válidos
#         | Usuario                  | 
#         | "jessica26"              |
#         |"jessicaluana26@gmail.com"|
#         | (92)988888888            |