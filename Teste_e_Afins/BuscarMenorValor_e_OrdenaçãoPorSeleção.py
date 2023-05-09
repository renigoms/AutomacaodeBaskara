def buscarmenor(arr: list):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


'''
A FUNÇÃO BUSCARMENOR VAI RECEBER UMA LISTA E
RETORNAR O MENOR VALOR PRESENTE NELA
'''


def ordenacaoporselecao(arr: list):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscarmenor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


lista = [22, 44, 36, 74, 809, 33, 2, 89]
print(ordenacaoporselecao(lista))
