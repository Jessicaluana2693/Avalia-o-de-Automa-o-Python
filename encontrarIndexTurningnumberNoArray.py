# Questão 5. Objetivo: Escreva uma função que encontra o index de um “turning number” em um array unimodal
# array {10, 9, 8, 7, 6, 1, 2, 3, 4, 5}
# O programa abaixo imprime o indice do menor valor em um vetor

lista = []
i = 0
quantidade = int( input('Tamanho do vetor: '))

while (i < quantidade):
    numero = input("Valor: ")
    i += 1
    lista.append(numero)

print(lista)
print ('Indice do menor valor:', lista.index(min(lista)))
