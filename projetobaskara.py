#FORMULA DE BHASKARA:
print('*'*30)
print('Formula de Bhaskara')
print('*'*30)
print('ax²+bx+c')
print('(-b±√(b^2-4ac))/2a')
print('*'*30)
a = int(input('Digite o valor de A>>'))
b = int(input('Digite o valor de B>>'))
c = int(input('Digite o valor de C>>'))
delta = (b**2 - 4*a*c)**(1/2)
print(f'Valor do delta:{delta}')
x1 = (-(b) + delta)/ (2*a)
x2 = (-(b) - delta)/ (2*a)
print('*'*30)
print(f'X1: {x1}')
print(f'X2: {x2}')
print('*'*30)
print('Você quer calcular o vetor?')
vetor = int(input('DIGITE 1 PARA SIM E 0 PARA NÃO:'))
print('*'*30)
bot = None
if vetor == 1:
    bot = True
else:
    bot = False
if bot:
    print('CALCULO DO VETOR')
    x = (-(b))/(2*a)
    y = -(delta) / (4*a)
    print(f'Vetor de X: {x}')
    print(f'Vetor de Y: {y}')
else:
    print('sem calculo do vetor.')
# CONCAVIDADE:
print('Quer ver a posição do gráfico?')
concaviade = int(input('DIGITE 1 PARA SIM E 0 PARA NÃO:'))
print('*'*30)
bot = None
if vetor == 1:
    bot = True
else:
    bot = False
if bot:
    print('CONCAVIDADE DO GRÁFICO')
    if a>0:
        print('concavidade para cima.')
    else:
        print('concavidade para baixo.')
else:
    print('certo, OBRIGADO POR USAR O PROGRAMA')
print('FIM DO PROGRAMA')





