empresa = 'marvel, o android paranoico'
lempresa = list(empresa)
for i in lempresa[:6:]:
    print(f'\t {i}')
print()
for i2 in lempresa[10:17]:
    print('\t'*2, i2)
print()
for i3 in lempresa[-9:]:
    print('\t' * 3, i3)
