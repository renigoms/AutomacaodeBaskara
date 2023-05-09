# DESENVOLVIMENTO DO PROGRAMA
print('-'*30, 'CONVERSOR DE UNIDADES', '-'*30)
print('unidades: metro,mquad e mcub')
vaconv = input('INDIQUE A UNIDADE DE CONVESÃO>>')
if vaconv == 'metro':
    print('--------------CONVERSÃO DO METRO----------------')
    metro = int(input('DIGITE QUALQUER NÚMERO EM METRO>>'))
    km = metro / 1000
    hm = metro / 100
    dam = metro / 10
    dm = metro * 10
    cm = metro * 100
    mm = metro * 1000
    print('{}M EQUIVALE A: \n{} KM; \n{}HM; \n{}DAM; \n{}DM; \n{}CM; \n{}MM;'.format(metro, km, hm, dam, dm, cm, mm))

if vaconv == 'mquad':
    print('*' * 20, 'CONVERÇÕES PARA METRO QUADRADO', '*' * 20)
    mquad = int(input('DIGITE QUALQUER NUMERO EM METROS QUADRADOS>>>'))
    kmquad = mquad / 1000000
    hmquad = mquad / 10000
    damquad = mquad / 100
    dmquad = mquad * 100
    cmquad = mquad * 10000
    mmquad = mquad * 1000000
    print('{}M² EQUIVALE A: \n{} KM²; \n{}HM²; \n{}DAM²; \n{}DM²; \n{}CM²; \n{}MM²;'.format(mquad, kmquad, hmquad,
                                                                                            damquad, dmquad, cmquad,
                                                                                            mmquad))

if vaconv == 'mcub':
    print('*' * 20, 'CONVERÇÕES PARA METRO CUBICO', '*' * 20)
    mcub = int(input('DIGITE QUALQUER NUMERO EM METROS CUBICOS>>>'))
    kmcub = mcub / 1000000000
    hmcub = mcub / 1000000
    damcub = mcub / 1000
    dmcub = mcub * 1000
    cmcub = mcub * 1000000
    mmcub = mcub * 1000000000
    print('{}M² EQUIVALE A: \n{} KM³; \n{}HM³; \n{}DAM³; \n{}DM³; \n{}CM³; \n{}MM³;'.format(mcub, kmcub, hmcub, damcub,
                                                                                            dmcub, cmcub, mmcub))
else:
    print('=' * 30, 'CONVERSOR DE KM PARA M', '=' * 30)
    KM = int(input('DIGITE QUALQUER NUMERO EM KM>>>'))
    M = KM * 1000
    print('{} quilometros, equivale a {} metros>>'.format(KM, M))





















