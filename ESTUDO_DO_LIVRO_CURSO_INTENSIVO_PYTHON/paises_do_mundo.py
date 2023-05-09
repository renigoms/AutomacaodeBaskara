# 3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
# você gostaria de visitar.
# • Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
# em ordem alfabética.
# • Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
# elegante; basta exibi-la como uma lista Python pura.
# • Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
# lista propriamente dita.
# • Mostre que sua lista manteve sua ordem original exibindo-a.
# • Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
# a ordem da lista original.
# • Mostre que sua lista manteve sua ordem original exibindo-a novamente.
# • Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
# que sua ordem mudou.
# • Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
# para mostrar que ela voltou à sua ordem original.
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

listapaises = ['Estados Unidos', 'Egito', 'Noruega', 'Vaticano', 'Grecia', 'Reino Unido']
print('lista normal')
print(listapaises)
print('lista com sorted sem alterar a ordem permanentimente')
print(sorted(listapaises))
print('prova disso')
print(listapaises)
print('lista com reverse, ou seja, ao contrario')
listapaises.reverse()

print(listapaises)
print('reverse para voltar a ordem original')
listapaises.reverse()

print(listapaises)
print('sort para deixar a lista em ondem alfabetica permanentimente')
listapaises.sort()

print(listapaises)
print('deixando o codigo em ordem alfabetica ao contrario')

listapaises.sort()
listapaises.reverse()
print(listapaises)
