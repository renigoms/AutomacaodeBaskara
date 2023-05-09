listanum = []
listapar = []
listaimpar = []
while True:
    listanum.append(int(input('DIGITE UM NÚMERO>>>')))
    op = input('QUER CONTINUAR? [s/n]').lower()
    if op == 'n':
        break
print(f'LISTA COMPLETA: {listanum}')
for i in listanum:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
print(f'OS NÚMEROS PARES SÃO: {listapar}')
print(f'OS NÚMEROS IMPARES SÃO: {listaimpar}')
