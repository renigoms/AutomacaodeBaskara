print('ESCOLA SANTA PARCIÊNCA')
NOTA1 = int(input('Coloque a Primeira nota 1:'))
NOTA2 = int(input('Coloque a Segunda nota 2:'))
NOTA3 = int(input('Coloque a Terceira nota 3:'))
print('PESO DAS NOTAS: 2,3 E 5')
peso1 = NOTA1 * 2
peso2 = NOTA2 * 3
peso3 = NOTA3 * 5
media = (peso1 + peso2 + peso3)/2*3*5
print('A média é: {}'.format(media))
