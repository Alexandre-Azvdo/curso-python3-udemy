import abc

class Conta(abc.ABC):    
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numero_conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        raise NotImplementedError('Implemente o médoto')
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')
        return self.saldo
    
    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('---')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name} {attrs}'


class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, numero_conta: int, 
        saldo: float = 0, limite: float = 0
    ):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name} {attrs}'
    

if __name__ == '__main__':
    cp = ContaPoupanca(111, 222)
    cp.sacar(1)
    cp.depositar(1)
    cp.sacar(1)
    cp.sacar(1)
    print('##')
    cc = ContaCorrente(111, 222, 0, 100)
    cc.sacar(1)
    cc.depositar(1)
    cc.sacar(1)
    cc.sacar(1)
    cc.sacar(98)
    cc.sacar(1)
   