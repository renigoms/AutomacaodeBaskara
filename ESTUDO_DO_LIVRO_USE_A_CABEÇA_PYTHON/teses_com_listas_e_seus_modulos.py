nome = 'renan'
lnome = list(nome)
print(nome)
print(lnome)
for i in range(0, 3):
    lnome.insert(0, lnome.pop())
lnome.insert(3, lnome.pop())
nomeinvertido = ''.join(lnome)
print(lnome)
print(nomeinvertido)


