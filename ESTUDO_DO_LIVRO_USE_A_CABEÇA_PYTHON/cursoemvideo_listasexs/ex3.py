listadevalores = []
flag = False
for i in range(5):
    num = int(input('DIGITE UM NUMERO'))
    if len(listadevalores) > 0:

        for x in range(len(listadevalores)):
            if num <= listadevalores[x]:
                listadevalores.insert(x, num)
                print(f'NUMERO ADICIONADO NA POSIÇÃO {x}')
                flag = True
                break
    if i == 0 or flag == False:
        listadevalores.append(num)
    else:
        flag = False
print(listadevalores)
