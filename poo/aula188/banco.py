from contas import Conta
from clientes import Cliente

class Banco():
    def __init__(self, contas: Conta, clientes: Cliente):
        self.contas = [contas]
        self.clientes = [clientes]
