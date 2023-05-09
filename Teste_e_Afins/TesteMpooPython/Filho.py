import Pai
import Mae

class Filho(Pai,Mae):
    def __init__(self, cpf, nome):
        super().__init__(nome)
        self.cpf = cpf