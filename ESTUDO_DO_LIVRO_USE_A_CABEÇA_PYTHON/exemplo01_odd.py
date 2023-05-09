from datetime import datetime
import time
import random
print('''
Programa que mostra se o 
minuto da hora atual é impar 
ou não
''')

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
        25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
        45, 47, 49, 51, 53, 55, 57, 59]

neste_minuto = datetime.today().minute
if neste_minuto in odds:
    print('este minuto é ímpar')
else:
    print('este minuto não é ímpar')


print('''
Programa que faz exatamente a mesma coisa 
vista acima porèm repetindo 5 vezes a cada 3 segundos 
e a cada vez, sorteia um numero entre 1 e 60
''')

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
        25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
        45, 47, 49, 51, 53, 55, 57, 59]

for i in range(0, 5):
    neste_minuto = datetime.today().minute
    if neste_minuto in odds:
        print('este minuto é ímpar')
    else:
        print('este minuto não é ímpar')
    segundos_aleatorios = random.randint(1, 60)
    time.sleep(segundos_aleatorios)
