class Pesssoa:

    def __init__(self, nome):
        self.nome = nome


    def __str__(self) -> str:
        return f"{self.nome}"



lista = [Pesssoa("renan"), Pesssoa("renata"), Pesssoa("afonso"), Pesssoa("zelia")]


def boubleSort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i.nome <= pivo.nome]
        maiores = [i for i in lista[1:] if i.nome > pivo.nome]
        return boubleSort(menores) + [pivo] + boubleSort(maiores)

novaLista = boubleSort(lista)
lista.clear()
for i in range(len(novaLista)):
    lista.append(novaLista[i])

def PesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:

        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute.nome == item:
            return meio
        elif chute.nome > item:
            alto = meio - 1

        else:
            baixo = meio + 1
    return None

for e in range(len(lista)):
    print(lista[e])
print(PesquisaBinaria(lista,"afonso"))
