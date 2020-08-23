# Questão 4. objetivo: Implementar o algoritmo do Bubble Sort em Python e utilizar este algoritmo
#para desenvolver um programa, que recebe uma string como entrada e
#ordena os valores informados.

# implementação do algoritmo
def sort(array):

    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break

#incerção dos valores no vetor
array = sorted([10,8,2,3,5,1]) # entrada: 10 8 2 3 5 1
sort(array) # classificando os elementos da lista em uma ordem crescente.
auxList = array # lista auxiliar que recebe o array de inteiros
strList = ' '.join(str(e) for e in auxList) # transformando a lista em string, concatenando e separando por espaços
print(strList) #saída: 1 2 3 5 8 10
