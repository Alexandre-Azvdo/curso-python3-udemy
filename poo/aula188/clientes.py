import contas
from pessoas import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.numero_conta: contas.Conta | None = None


if __name__ == '__maim__':

    c1 = Cliente('Alexandre', 39)
    c1.numero_conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.numero_conta)
    c2 = Cliente('Gustavo', 5)
    c2.numero_conta = contas.ContaPoupanca(112, 333, 100)
    print(c2)
    print(c2.numero_conta)

