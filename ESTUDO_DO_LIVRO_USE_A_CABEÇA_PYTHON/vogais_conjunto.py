# vogais = set('aeiou')
# palavra = input('digite uma palavra qualquer>>>').lower()
# found = vogais.intersection(set(palavra))
# for vogal in found:
#     print(vogal)


# ESSE PROGRAMA IDENTIFICA, DE TRÁS PARA FRENTE, SE HÁ VOGAIS NA PALAVRA E AS PRINTA NA TELA

def search4vowels(phrase: str) -> set:
    # FUNÇÃO PARA VERIFICAR SE EXISTEM VOGAIS
    # EM QUALQUE PALAVRA QUE VC JOGAR COMO PARAMETRO DA FUNÇÃO
    """
    str e ->set servem apenas como anotações e não determinam o tipo da variável
    apenas sugerem o que é esperado
    """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4vowels2(pharase: str, letters: str) -> set:
    return set(letters).intersection(set(pharase))
'''
ESSA FUNÇÃO VERIFICA SE QUALQUER CONJUNTO DE LETRAS QUE VOCÊ PASSAR
EXISTE NA PALAVRA QUE VOOCÊ PASSAR.
'''

print(search4vowels('renan'))
print(f'segunda função: {search4vowels2("paralelepipedo", "pna")}')
