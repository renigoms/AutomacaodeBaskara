listanum = []
mai = 0
men = 0
for i in range(0, 5):
    listanum.append(int(input(f'DIGITE O {i + 1}° NÚMERO>>')))
    # MAIOR VALOR E MENOR VALOR OUTRA FORMA DE FAZER:
    if i == 0:
        mai = men = listanum[i]
    else:
        if listanum[i] > mai:
            mai = listanum[i]
        if listanum[i] < men:
            men = listanum[i]
print(f'VOCÊ DIGITOU OS VALORES: {listanum}')
print(f'O MAIOR VALOR DIGITADO FOI O {mai} NAS POSIÇÕES: ', end='')
for i, o in enumerate(listanum):
    if o == mai:
        print(f'{i}...', end='')
print()
print(f'O MENOR VALOR DIGITADO FOI O {men} NAS POSIÇÕES: ', end='')
for i, o in enumerate(listanum):
    if o == men:
        print(f'{i}...', end='')

