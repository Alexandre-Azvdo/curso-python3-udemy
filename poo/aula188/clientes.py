from contas import Conta

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.nome
    
    @property
    def idade(self):
        return self.idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta

