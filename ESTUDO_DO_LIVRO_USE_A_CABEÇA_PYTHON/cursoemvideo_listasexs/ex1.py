print('''\033[36m
*Faça um programa que leia 5 valores númericos 
e aramzene em uma lista.
* No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista.\033[m
''')
listavn = []
listaindice = []
maior = 0
menor = 0
cont = 0
for i in range(5):
    print('*'*5, '\t\033[31m VALORES NÚMERICOS \033[m\t', '*'*5)
    valor = int(input('Digite um valor númerico >>>>'))
    listavn.append(valor)
    if valor > maior:
        maior = valor

    if valor < menor or menor == 0:
        menor = valor
print('\033[32m=\033[m'*40)
print('\t', '*'*5, '\t\033[31m VALORES NÚMERICOS \033[m\t', '*'*5)
print('\033[32m=\033[m'*40)
print(f' \t\tValores digitados : {listavn}')
print('\033[32m=\033[m'*40)
print(f'\tO maior valor digitado foi o {maior} nas posições: ', end='')
for i, o in enumerate(listavn):
    if o == maior:
        print(f'{i}...', end='')
print()
print(f'\tO menor valor digitado foi o {menor} nas posições: ', end='')

for i, o in enumerate(listavn):
    if o == menor:
        print(f'{i}...', end='')

