lsvalores = []
while True:
    print('=+'*10, 'VALORES NUMERICOS', '=+'*10)
    valores = int(input('DIGITE UM VALOR NUMERICO>>>'))
    if valores in lsvalores:
        print('ESSE VALOR JÁ EXISTE.')
    else:
        lsvalores.append(valores)
    op = input('QUER CONTINUAR? [s/n]').upper()
    if op == 'S':
        continue
    else:
        break


lsvalores.sort()

print(f'VOCÊ DIGITOU: {lsvalores}')
