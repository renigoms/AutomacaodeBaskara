print('repete vogais uma vez')
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = 'vamos ver se isso funciona'
for letras in vogais:
    if letras in palavra:
        print(letras)

print('repete vogais varias vezes')
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = 'vamos ver se isso funciona'
for letras in palavra:
    if letras in vogais:
        print(letras)

print('COMO ESTÁ NO LIVRO (MAIS OU MENOS)')
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = 'vamos ver se isso funciona'
found = []
for letras in palavra:
    if letras in vogais:
        if letras not in found:
            found.append(letras)
for letras in found:
    print(letras)







