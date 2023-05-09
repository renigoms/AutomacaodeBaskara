import addinfo
while True:
    print('''
        MENU DO TESTE DATAS
        [1]-CADASTRO DATAS
        [2]- SAIR
    ''')

    op = int(input('DIGITE UMA DAS OPÇÕES>>>'))

    if op == 1:
        addinfo.cadastro()
    elif op == 2:
        print('OBRIGADO POR USAR O PROGRAMA!!!')
        break