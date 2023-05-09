def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        maiores = [i for i in lista[1:] if i >= pivo]
        menores = [i for i in lista[1:] if i < pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


def soma(list):
    if not list:
        return 0
    else:
        return list[0] + soma(list[1:])


lista = [1, 2, 3]
print(soma(lista))
