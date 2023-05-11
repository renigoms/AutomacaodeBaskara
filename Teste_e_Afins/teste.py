class SuperClass:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome

 
class SuperClass2:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome2(self):
        return self.nome


class SubClass(SuperClass, SuperClass2):
    def __init__(self, nome1: str, nome2: str, nome3:str):
        super().__init__(nome2)
        super().__init__(nome3)
        self.nome1 = nome1

    def __str__(self):
        return f"{self.nome1} e {self.getNome()} e {self.getNome2()}"


subClasse = SubClass("renan", "renata", "Afonso")

print(subClasse)
