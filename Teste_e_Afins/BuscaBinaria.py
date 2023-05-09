def busacabinaria(lista, item):
    baixo = 0
    alto = len(lista)
    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
teste = []
for i in range(1,11):
    teste.append(i)

print(busacabinaria(item=9, lista=teste))