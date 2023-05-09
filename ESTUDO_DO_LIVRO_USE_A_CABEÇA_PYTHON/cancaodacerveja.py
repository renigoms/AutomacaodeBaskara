word_palavra = 'bottles/garrafas'
for beer_num_numcervejas in range(99, 0, -1):
    print(beer_num_numcervejas, word_palavra, 'of beer on the wall./de cerveja na parede.')
    print(beer_num_numcervejas, word_palavra, 'of beer./de cerveja.')
    print('take one down. / derrube um.')
    print('pass it around. / passá-lo ao redor.')
    if beer_num_numcervejas == 1:
        print('no more bottles of beer on the wall./não há mais garrafas de cerveja na parede.')
    else:
        new_num_novonum = beer_num_numcervejas - 1
        if new_num_novonum == 1:
            word_palavra = 'bottles/garrafas'
        print(new_num_novonum, word_palavra, 'of beer on the wall./de cerveja na parede.')
    print()


