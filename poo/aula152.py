# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro recebemos a própira classe.
class Pessoa:
    ano = 2024  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('Gustavo', 5)
# print(Pessoa.ano)
# p1.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos('Alexandre')
p3 = Pessoa.criar_sem_nome(34)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
