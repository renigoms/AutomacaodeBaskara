# variaveis;
listinfo = []
opcao = None
op2=None
op=None
a=None
salvar=[]
fones=[]
lista=[]
# adição de informações;
def cadastro():
        while True:

            print('|       CADSTRAR NOVO CONTATO     |')


            nome = input('|NOME DO CONTATO:')

            print('-' * 35)
            numero = input('|NUMERO(s)) DO CONTATO:')

            # agrupamento de informações;

            print('-' * 35)
            # opcao de cadastrar outro contato ou não;
            print('+++++++++++++++++++++++')
            break




        op = input('QUER ADICIONAR MAIS UM telefone?: [s/n]').upper()
        if op == 'S':
            while True:
                N1 = input('digite o número')
                fones=[N1]
                lista.append(fones)
                op2 = input('QUER ADICIONAR MAIS UM?: [s/n]').upper()
                if op2 != 'S':
                    break
        opcao = int(input('QUER CADASTRAR MAIS UM CONTATO? [1]-SIM E [2]-NÃO: '))
        if opcao == 1:
            return cadastro()

        listinfo = [nome, numero, lista]
        salvar.append(listinfo)
cadastro()
#=============================================================
r = range(0, len(salvar))
print('*'*15,'LISTA DE CONTATOS','*'*15)

for i in r:

    print(f'{i+1}° CONTATO')


    print(f'/ NOME DO CONTATO: {salvar[i][0]}')

    print(f'NÚMERO DO CONTATO: {salvar[i][1]} ')
    print(f'NÚMERO extra: {salvar[i][2]} ')
    cont=1

    while cont<len(lista):
        cont+=1
        b=lista[0:cont]
        print(b)