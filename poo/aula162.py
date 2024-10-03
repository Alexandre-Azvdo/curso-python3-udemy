# Herança simples - Relações entre classes
# Associação -> usa
# Agregação  -> tem
# Composição -> é dono de
# Herança    -> é um 
#
# Herança ou Composição
# 
# Classe principal (Pessoa)
#   -> super class, base class, parent cçass
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = '123.456.789-00'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('Executou a função da classe pai')
        print(self.__class__.__name__, self.nome, self.sobrenome)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Executou a função da classe filha')
        print(self.__class__.__name__, self.nome, self.sobrenome)

class Aluno(Pessoa):
    cpf = '000.000.000-00'


c1 = Cliente('Alexandre', 'Azevedo')
print('CPF:', c1.cpf)
c1.falar_nome_classe()

print()
a1 = Aluno('Gustavo', 'Rafael')
print('CPF:', a1.cpf)
a1.falar_nome_classe()
