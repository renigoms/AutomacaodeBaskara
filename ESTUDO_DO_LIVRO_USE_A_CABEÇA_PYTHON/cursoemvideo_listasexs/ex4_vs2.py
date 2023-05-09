listanum = []
while True:
    listanum.append(int(input('DIGITE UM NÚMERO>>>')))
    op = input('QUER CONTINUAR? [s/n]').lower()
    if op == 'n':
        break
print(f'ESTA LISTA POSSUI {len(listanum)} ELEMENTOS')
listanum.sort(reverse=True)
print(f'LISTA NA ORDEM DECRECENTE: {listanum}')
if 5 in listanum:
    print('O NÚMERO 5 ESTÁ NESSA LISTA')
else:
    print('O NÚMERO 5 NÃO ESTÁ NESTA LISTA')
