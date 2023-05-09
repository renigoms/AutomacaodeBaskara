vogais = ['a', 'e', 'i', 'o', 'u']
palavra = 'vamos ver se isso funciona'
found = []
for letras in palavra:
    if letras in vogais:
        if letras not in found:
            found.append(letras)
for letras in found:
    print(letras)