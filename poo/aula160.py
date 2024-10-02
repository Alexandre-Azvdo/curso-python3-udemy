# Relações entre classes: associação. agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são apagadas.
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO ENDEREÇO', self.rua, self.numero)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self,endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO CLIENTE', self.nome)

cliente = Cliente('Alexandre')
cliente.inserir_endereco('Rua Pedro Francisco Maciel', 904)
cliente.inserir_endereco('Rua Vereador Elias Duarte', 691)
endereco_externo = Endereco('Rua A', 245)
cliente.inserir_endereco_externo(endereco_externo)

cliente.listar_enderecos()
del cliente

print(endereco_externo.rua, endereco_externo.numero)

print('\nAqui termina meu código\n')
