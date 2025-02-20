# dataclasses - O que são dataclasses?
# O módulo dataclass fornece um decorador e funções para criar métodos como
# __init__(), __repr_(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclases são 'syntax sugar' para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Pythin.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(init=False)
class Pessoa:
    nome: str 
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Alexandre', 'Azevedo')
    
    print(p1)
    print(p1.nome_completo)
