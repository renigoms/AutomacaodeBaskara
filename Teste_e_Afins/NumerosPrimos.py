def quantnum():
    primos = []
    numero = int(input('\033[1:32m Digite um número do conjunto dos números naturais(números > 0)>>>'))
    if numero > 0:
        for i in range(numero, 0, -1):
            if i % 2 != 0 or i % 3 != 0 and i % i == 0 and i%1 == 0:
                primos.append(i)

        return print(f'Numeros primos : {primos}')
    else:
        raise Exception('ESSE NÚMERO NÃO É UN NÚMERO NATURAL')
quantnum()

