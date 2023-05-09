# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
# crie uma lista contendo esses itens e então utilize cada função apresentada
# neste capítulo pelo menos uma vez.


print()
convidados_do_jantar = []
print('escolha três pessoas para o jantar.')
cont = 0
while True:
    nomes = input(f'{cont + 1} pessoa: ')
    nomes = nomes.title()
    cont += 1
    convidados_do_jantar.append(nomes)
    if cont == 3:
        break
print(convidados_do_jantar)
print(f'{convidados_do_jantar[0]}, venha jantar comigo.')
print(f'{convidados_do_jantar[1]}, quer jantar comigo?')
print(f'{convidados_do_jantar[2]}, hoje o jantar è comigo. Topa?')
input()

print('Puxa, alguém não vai vim.')
naovaivim = input('QUEM SERÁ?')
naovaivim = naovaivim.title()
localizacao = convidados_do_jantar.index(naovaivim)
convidados_do_jantar.remove(naovaivim)
novapessoa = input(f'QUEM VAI VIM NO LUGAR DE {naovaivim}?')
novapessoa = novapessoa.title()
convidados_do_jantar.insert(localizacao, novapessoa)
print()
print(convidados_do_jantar)
print(f'{convidados_do_jantar[0]}, venha jantar comigo.')
print(f'{convidados_do_jantar[1]}, quer jantar comigo?')
print(f'{convidados_do_jantar[2]}, hoje o jantar è comigo. Topa?')
print()


print('EITA, A MESA TEM ESPAÇO PARA MAIS 3 PESSOAS')
cont = 0
while True:
    nomes = input(f'{cont + 1} pessoa: ')
    nomes = nomes.title()
    cont += 1
    if cont == 1:
        convidados_do_jantar.insert(0, nomes)
    elif cont == 2:
        convidados_do_jantar.insert(2, nomes)
    elif cont == 3:
        convidados_do_jantar.append(nomes)
        break

print(f'{convidados_do_jantar[0]},{convidados_do_jantar[2]} e {convidados_do_jantar[-1]} encontrei uma mesa maior '
      f'aqui, venham.')
print(convidados_do_jantar)
print('lista com sorted sem alterar a ordem permanentimente')
print(sorted(convidados_do_jantar))
print('prova disso')
print(convidados_do_jantar)
print('lista com reverse, ou seja, ao contrario')
convidados_do_jantar.reverse()

print(convidados_do_jantar)
print('reverse para voltar a ordem original')
convidados_do_jantar.reverse()

print(convidados_do_jantar)
print('sort para deixar a lista em ondem alfabetica permanentimente')
convidados_do_jantar.sort()

print(convidados_do_jantar)
print('deixando o codigo em ordem alfabetica ao contrario')

convidados_do_jantar.sort()
convidados_do_jantar.reverse()
print(convidados_do_jantar)
input()

input()
print('EITA P****, A MESA NÃO VAI CHEGAR A TEMPO!!!!'
      'SÓ VAI TER ESPAÇO PARA DUAS PESSOAS!!!'
      'E AGORA ?')
input()
cont = 0
while True:
    print()
    removido = convidados_do_jantar.pop()
    cont += 1
    print(f'infelismente não deu certo {removido} sinto muito')
    print()

    if cont == 4:
        break

print(f'nova lista: {convidados_do_jantar}')

print('deletando a lista')
del convidados_do_jantar[0]
del convidados_do_jantar[0]
print(convidados_do_jantar)
input()