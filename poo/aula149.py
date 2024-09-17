# Atributos de classe
ANO_ATUAL = 2022

class Pessoa:
    
    ano_atual = 2024    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Alexandre', 39)
p2 = Pessoa('Gustado', 5)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())