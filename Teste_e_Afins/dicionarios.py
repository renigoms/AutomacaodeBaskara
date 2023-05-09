DicTest = {
      'nome': 'renan',
      'idade': 19,
      'corfavorita': 'azul',
}
DicTest2 = {
      'nome': 'renata',
      'idade': 16,
      'corfavorita': 'rosa',
}

ListaDic = [DicTest, DicTest2]


print(ListaDic[0]['idade'])
del ListaDic[0]['nome']
print(ListaDic)
ListaDic[0]['nome'] = 'renan'
print(ListaDic)
