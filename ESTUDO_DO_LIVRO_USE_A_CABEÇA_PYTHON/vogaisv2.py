dicvogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,

}
pl = input('digite uma palvra: ').lower()

for i in pl:
    if i in dicvogais.keys():
        dicvogais[i] += 1
for c, v in sorted(dicvogais.items()):
    print(f'A VOGAL {c} NA PALAVRA {pl} APARECE {v} VEZES')

