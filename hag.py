import json


def gravar(x):
    with open('bd_dicionario', 'w') as bdjson:
        json.dump(x, bdjson, indent=2)


def ler():
    with open('bd_dicionario', 'r+') as bdjson:
        dicionario = json.load(bdjson)
        print(dicionario)
