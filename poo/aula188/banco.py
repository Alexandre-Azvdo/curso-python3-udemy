from re import split
import clientes
import contas
import pessoas


class Banco():
    def __init__(
            self, 
            agencias: list[int] | None = None, 
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None, 
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.numero_conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: clientes.Cliente, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and\
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':

    c1 = clientes.Cliente('Alexandre', 39)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.numero_conta = cc1

    c2 = clientes.Cliente('Gustavo', 5)
    cp2= contas.ContaPoupanca(112, 333, 100)
    c2.numero_conta = cp2

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp2])
    banco.agencias.extend([111, 222])


    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.numero_conta.depositar(100)
        print(c1.numero_conta)
    