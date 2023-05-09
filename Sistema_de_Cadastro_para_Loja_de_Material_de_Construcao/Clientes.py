import json


class Clientes:
    def __init__(self):
        self.nomecompleto = None
        self.apelido = None
        self.telefone = None

    def cadastrarclietes(self):
        self.nomecompleto = input("Digite seu nome completo>>>")
        self.apelido = input("Digite um apelido seu se ouver>>")
        self.telefone = input("Digite seu telefone>>>")
        self._salvarclientes()

    def _salvarjson(self, dicio_dados):
        with open("ClientesCadastrados.json", "w") as arquijson:
            json.dump(dicio_dados, arquijson, indent=3)

    def _lerjson(self):
        with open("ClientesCadastrados.json", "r+") as arquijson:
            novo_dicionario = json.load(arquijson)
            return novo_dicionario

    def _salvarclientes(self):
        dicio_dados = self._lerjson()
        dicio_dados[self.apelido] = {
            "nome": self.nomecompleto,
            "apelido": self.apelido,
            "telefone": self.telefone
        }
        self._salvarjson(dicio_dados)
        print("CLIENTE SALVO COM SUCESSO")


cliente = Clientes()
cliente.cadastrarclietes()