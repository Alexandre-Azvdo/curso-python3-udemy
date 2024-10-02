# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome, ano,  Motor, Fabricante):
        self.nome = nome
        self.ano = ano
        self.motor = Motor
        self.fabricante = Fabricante.nome
    
    def mostrar_descricao(self):
        print(f'Carro: {self.nome}\n\tAno: {self.ano}\n\tMotor: {self.motor.nome}\n\t{self.fabricante}')


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self, Carro):
        self.carros.append(Carro)

    def mostrar_carros(self):
        print(f'{self.nome}:')
        for carro in self.carros:
            print(f'\t{carro.nome}')

motor1 = Motor('V8')
fabricante1 = Fabricante('Ford')

carro1 = Carro('Maverick', 1976, motor1, fabricante1)
carro2 = Carro('Onix', 2024, motor1, fabricante1)
carro3 = Carro('Spin', 2022, motor1, fabricante1)

fabricante1.inserir_carro(carro1)
fabricante1.inserir_carro(carro2)
fabricante1.inserir_carro(carro3)

fabricante1.mostrar_carros()
print('#####################')
carro1.mostrar_descricao() 
carro2.mostrar_descricao() 
carro3.mostrar_descricao() 
