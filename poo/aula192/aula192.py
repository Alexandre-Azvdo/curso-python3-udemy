# dataclasses - O que são dataclasses?
# O módulo dataclass fornece um decorador e funções para criar métodos como
# __init__(), __repr_(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclases são 'syntax sugar' para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Pythin.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(repr=True)
class Pessoa:
    nome: str 
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
